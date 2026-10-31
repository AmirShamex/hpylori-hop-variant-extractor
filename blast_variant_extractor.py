#!/usr/bin/env python3
"""
Automated BLAST Sbjct Alignment Extractor & Variant Assembler
Tailored for: H. pylori OMP screening (AlpA, AlpB, BabA, HopZ, SabA)
Author: Seyed Amirhossein Shamekhi (@AmirShamex)
"""

import argparse
import re
import sys
from pathlib import Path


def parse_blast_report(raw_text: str, strip_gaps: bool = False):
    """
    Parses NCBI pairwise BLAST (format 0) output.
    Extracts alignment metadata and concatenates subject sequence blocks.
    """
    # 1. Extract Target Subject / Contig ID
    subject_match = re.search(r">(\S+)", raw_text)
    subject_id = subject_match.group(1) if subject_match else "Unknown_Subject"

    # 2. Extract Range coordinates
    range_match = re.search(r"Range\s+\d+:\s+(\d+)\s+to\s+(\d+)", raw_text)
    range_str = f"{range_match.group(1)}..{range_match.group(2)}" if range_match else "N/A"

    # 3. Extract Strand
    strand_match = re.search(r"Strand:\s*([A-Za-z]+/[A-Za-z]+)", raw_text)
    strand = strand_match.group(1) if strand_match else "Unknown"

    # 4. Extract Identity %
    ident_match = re.search(r"Identities:\s*(\d+/\d+\s*\(\d+%\))", raw_text)
    identities = ident_match.group(1) if ident_match else "N/A"

    # 5. Extract all Sbjct sequence blocks
    sbjct_parts = re.findall(r"Sbjct\s+\d+\s+([A-Za-z\-]+)\s+\d+", raw_text)
    if not sbjct_parts:
        return None, None

    seq = "".join(sbjct_parts)
    if strip_gaps:
        seq = seq.replace("-", "")

    metadata = {
        "subject_id": subject_id,
        "range": range_str,
        "strand": strand,
        "identities": identities,
        "length": len(seq),
    }

    return seq, metadata


def main():
    parser = argparse.ArgumentParser(
        description="Extract and concatenate Sbjct sequences from BLAST reports with metadata extraction."
    )
    parser.add_argument("-i", "--input", required=True, help="Path to raw BLAST report text file.")
    parser.add_argument("-o", "--output", help="Path to output FASTA file (default: STDOUT).")
    parser.add_argument("--gene", default="Target_Gene", help="Gene symbol prefix for the FASTA header.")
    parser.add_argument(
        "--strip-gaps", action="store_true", help="Remove indel gap characters (-) from sequence."
    )

    args = parser.parse_args()

    input_file = Path(args.input)
    if not input_file.is_file():
        sys.exit(f"[ERROR] Input file '{args.input}' not found.")

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    seq, meta = parse_blast_report(content, strip_gaps=args.strip_gaps)

    if not seq:
        sys.exit("[WARNING] No Sbjct alignment segments detected in the file.")

    # Construct rich academic FASTA header
    fasta_header = (
        f">{args.gene}_{meta['subject_id']} | Range={meta['range']} "
        f"| Strand={meta['strand']} | Identity={meta['identities']} | Length={meta['length']}bp"
    )
    fasta_output = f"{fasta_header}\n{seq}\n"

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(fasta_output)
        print(f"[SUCCESS] Extracted sequence saved to: {args.output}")
    else:
        print(fasta_output)


if __name__ == "__main__":
    main()