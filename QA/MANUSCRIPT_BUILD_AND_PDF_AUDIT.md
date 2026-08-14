# Manuscript Build and PDF Audit

On 13 August 2026, the four available publication LaTeX sources were copied into an
isolated clean-build directory and compiled with two `pdflatex` passes each.

| Object | Compile pass 1 | Compile pass 2 | PDF pages | Undefined citations/references |
|---|---:|---:|---:|---:|
| Paper 1 | PASS | PASS | 9 | 0 |
| Paper 2 | PASS | PASS | 9 | 0 |
| Paper 3 | PASS | PASS | 8 | 0 |
| Geatomica monograph | PASS | PASS | 136 | 0 |
| Public Technical Companion V1.5 | PASS | PASS | 11 | 0 |

PDF text extraction covered all 173 publication pages. No local Windows path, private
estate-root string, founder-review marker or private V1.1 companion identifier was found
in extracted manuscript text. All LaTeX-referenced figures exist in the release.

The public Technical Companion V1.5 is included with its publication source. It was
preflighted, text-extracted and visually inspected across all 11 pages; editable source
was not required or included. Its SHA-256 is
`907c222b5d2b0d4b5e225d77525429fd7306db80c4817c1df318e44a0f32cbce`.
