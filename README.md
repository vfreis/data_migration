<h1 align="center">Data Migration & File Profiling Toolkit</h1>

<p align="center">
  Python utilities for inspecting heterogeneous CSV and spreadsheet sources before transformation or migration.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/CSV-0F766E?style=for-the-badge" alt="CSV" />
  <img src="https://img.shields.io/badge/Data_Migration-7C3AED?style=for-the-badge" alt="Data migration" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Source_Profiling-0369A1?style=flat-square" alt="Source profiling" />
  <img src="https://img.shields.io/badge/Checks-Encoding_%26_Delimiters-F59E0B?style=flat-square" alt="Encoding and delimiter checks" />
  <img src="https://img.shields.io/badge/Status-Portfolio_Project-16A34A?style=flat-square" alt="Portfolio project" />
</p>

---

## Overview

Data migrations often fail before transformation begins because source files contain inconsistent encodings, delimiters, schemas, field types, or unreadable records.

This repository contains Python utilities for performing a **pre-migration inspection** of CSV and spreadsheet sources. The scripts identify file characteristics, attempt controlled reads, record issues, and produce structured information that can guide mapping and transformation work.

> This project focuses on source discovery and profiling. It does not currently implement a complete source-to-target migration engine.

---

## Problem Addressed

Before migrating data, an engineer needs to answer questions such as:

- Which files are present in the source directory?
- Which file formats need to be supported?
- What encoding is each CSV using?
- Which delimiter is present?
- Can the files be parsed successfully?
- What columns and inferred data types exist?
- Which sources require manual investigation before transformation?

The utilities in this repository automate part of that discovery process.

---

## Profiling Workflow

```text
Source directory
       │
       ▼
File discovery
       │
       ▼
Format identification
       │
       ├───────────────┐
       ▼               ▼
CSV sources       Excel sources
       │               │
       ▼               ▼
Encoding and      Workbook read
separator checks        │
       └───────┬───────┘
               ▼
Schema and type inspection
               │
               ▼
Structured logging and report data
               │
               ▼
Migration planning and transformation design
```

---

## Capabilities Represented

### File discovery

The scripts scan the working directory and identify supported source files, including CSV and spreadsheet formats.

### Encoding detection

CSV bytes are sampled and evaluated with `chardet` to estimate the source encoding before parsing.

### Delimiter inference

`csv.Sniffer` is used to inspect a sample and infer the separator where possible, with a fallback delimiter when detection is inconclusive.

### Schema profiling

A limited number of rows are loaded with Pandas so the utilities can capture:

- column names;
- inferred data types;
- read status;
- parsing or encoding errors.

### Structured logging

The workflow logs the file being inspected, detected characteristics, read status, and error conditions to make investigation easier.

### Spreadsheet inspection

Additional logic identifies CSV, XLSX, and XLS files and prints available columns and inferred types.

---

## Technologies

| Area | Technologies |
|---|---|
| Language | Python |
| Tabular processing | Pandas |
| Encoding detection | chardet |
| CSV inspection | Python `csv` module |
| Spreadsheet support | Pandas, OpenPyXL-compatible workflows |
| Operational visibility | Python logging |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vfreis/data_migration.git
cd data_migration
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install the libraries used by the utilities

```bash
pip install pandas chardet openpyxl
```

### 4. Prepare source files

Place test CSV or spreadsheet files in the working directory used by the profiling scripts.

### 5. Run the relevant profiling utility

Execute the script that matches the type of inspection needed from the repository root.

> Review source files before execution. Real migration data may contain confidential or regulated information and should not be committed to a public repository.

---

## Example Output Structure

The CSV profiling logic builds report entries with information equivalent to:

```python
{
    "arquivo": "source.csv",
    "colunas": ["column_a", "column_b"],
    "tipos_dados": {
        "column_a": "int64",
        "column_b": "object"
    },
    "status": "Lido com sucesso"
}
```

When parsing fails, the status records the relevant encoding, parser, or unexpected error.

---

## Skills Demonstrated

- Source-system discovery.
- Defensive file ingestion.
- Encoding and delimiter handling.
- Schema and data-type profiling.
- Structured error handling.
- Logging for migration diagnostics.
- Preparing heterogeneous sources for mapping and transformation.
- Separating inspection from downstream migration logic.

---

## Security and Data Handling

Migration repositories should never expose real client or company data.

Recommended safeguards:

- use synthetic or anonymized samples;
- exclude source files through `.gitignore`;
- keep credentials and connection strings outside the repository;
- avoid logging personal or confidential field values;
- document retention and deletion rules for temporary extracts;
- validate target mappings before loading production systems.

---

## Limitations

- The repository currently focuses on local file profiling.
- It does not yet generate a complete persistent report file.
- Schema inference is based on limited samples and may not represent the entire dataset.
- Encoding detection is probabilistic and should be validated for critical migrations.
- The project does not currently provide automated tests, a CLI, or source-to-target loading.

---

## Roadmap

- Add a project-specific `requirements.txt`.
- Consolidate utilities behind a command-line interface.
- Export profiling results as JSON and CSV reports.
- Add configurable file-size and row-sampling limits.
- Add full-column quality statistics and null-rate analysis.
- Add schema comparison between source files.
- Add automated tests with synthetic fixtures.
- Add mapping templates for source-to-target design.
- Add optional database source profiling as a separate module.

---

## Author

**Vinicios Falqueiro Reis** — Data Engineer focused on reliable ingestion, data preparation, and migration-oriented workflows.

[LinkedIn](https://www.linkedin.com/in/vfalqueiroreis/) · [GitHub](https://github.com/vfreis)