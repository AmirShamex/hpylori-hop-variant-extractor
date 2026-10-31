# BLAST Pairwise Alignment Parser & Microbial Variant Assembler

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)

A command-line Python utility engineered to parse NCBI pairwise BLAST reports (Format 0), automate multi-block alignment assembly, extract genomic coordinate metadata, manage indels, and export standardized FASTA sequences for downstream variant profiling and phylogenetics.

---

## Scientific Background

*Helicobacter pylori* outer membrane proteins (OMPs) mediate host epithelial cell adhesion, colonization persistence, and virulence modulation. During genomic research at Shahid Beheshti University, 31 whole-genome sequenced (WGS) clinical *H. pylori* isolates from Iranian patients were screened to discover novel allelic variants across five major adhesin loci: *alpA*, *alpB*, *babA*, *hopZ*, and *sabA*.

Reference sequences were obtained from *H. pylori* strain MT5135 (*alpA*, *alpB*, *babA*, *sabA*) and strain 26695 (*hopZ*). All assembly contigs were searched using BLAST with thresholds of $\ge 95\%$ coverage and $\ge 85\%$ sequence identity.

### Genomic Discovery Output
This automated parsing engine supported the discovery, assembly, and submission of **76 novel non-redundant alleles** deposited into the NCBI GenBank repository:
* **`alpA`**: 30 novel alleles identified
* **`alpB`**: 27 novel alleles identified
* **`hopZ`**: 28 novel alleles identified
* **`sabA`**: 21 novel alleles identified
* **`babA`**: 5 novel alleles identified

This work was presented at the *6th International & 18th Iranian Genetics Congress (GC2024)* (Abstract G-1201).

---

## Features

* **Multi-Block Regex Assembly:** Traverses pairwise BLAST text reports and concatenates discontinuous `Sbjct` sequence blocks across multi-page alignments.
* **Genomic Metadata Extraction:** Automatically extracts contig IDs (`>ID`), range coordinates (`Range: Start to End`), strand orientations (`Plus/Plus` or `Plus/Minus`), and percentage identities.
* **Indel Management (`--strip-gaps`):** Detects and removes alignment gap characters (`-`) to produce an uninterrupted nucleotide sequence ready for in-frame translation.
* **Standardized FASTA Generation:** Wraps assembled sequences into NCBI-compliant FASTA entries with structural annotations.

---

## Usage & Benchmark Example

Screening an authentic clinical *H. pylori* draft assembly (148 contigs) for the *alpA* locus:

```bash
# Clone repository
git clone [https://github.com/AmirShamex/hpylori-hop-variant-extractor.git](https://github.com/AmirShamex/hpylori-hop-variant-extractor.git)
cd hpylori-hop-variant-extractor

# Execute parser
python blast_variant_extractor.py \
  -i example_data/HPC2_AlpA.txt \
  -o results/HPC2_AlpA_extracted.fasta \
  --gene "AlpA" \
  --strip-gaps
```
## Conference Citations

If utilizing or adapting these analytical pipelines, please cite the corresponding conference presentation:

 **Najafi Disfani, M. R.**, **Shamekhi, S. A.**, **Razkhaneh, M.**, & **Saniee, P.** (2024, July 7–9). *Identification of novel variants in Hop adhesion gene family in Iranian Helicobacter pylori isolates through whole genome sequencing* [Poster Presentation]. 6th International & 18th Iranian Genetics Congress (GC2024), Shahid Beheshti University, Tehran, Iran. Abstract Code: G-1201.

---

## License & Contact

* **License:** Distributed under the [MIT License](LICENSE).
* **Author:** Seyed Amirhossein Shamekhi
* **Affiliation:** Department of Microbiology and Microbial Biotechnology, Shahid Beheshti University, Tehran, Iran
* **GitHub:** [@AmirShamex](https://github.com/AmirShamex)
* **LinkedIn:** [Amirhossein Shamekhi](https://linkedin.com/in/amirshamekhi)
* **Email:** [amirhshamekhi@gmail.com](mailto:amirhshamekhi@gmail.com)
