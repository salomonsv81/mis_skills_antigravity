---
name: xlsx
description: "Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization."
license: Proprietary
---

# XLSX Creation, Editing, and Analysis

## Requirements for All Excel Files

### Zero Formula Errors
Every Excel model MUST be delivered with ZERO formula errors (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

## Reading and Analyzing Data

```python
import pandas as pd

# Read Excel
df = pd.read_excel('file.xlsx')  # Default: first sheet
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # All sheets as dict

# Analyze
df.head()      # Preview data
df.info()      # Column info
df.describe()  # Statistics
```

## Creating/Editing with openpyxl

```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
sheet = wb.active

# Add data and formula
sheet['A1'] = 'Revenue'
sheet['B1'] = 1000
sheet['B2'] = '=SUM(B1:B10)'  # Use formulas, not hardcoded values!

# Formatting
sheet['A1'].font = Font(bold=True)
sheet['A1'].fill = PatternFill('solid', start_color='FFFF00')

wb.save('output.xlsx')
```

## CRITICAL: Use Formulas, Not Hardcoded Values

**Always use Excel formulas instead of calculating values in Python and hardcoding them.**

```python
# ❌ WRONG - Hardcoding
sheet['B10'] = 5000  # Hardcoded result

# ✅ CORRECT - Using formulas
sheet['B10'] = '=SUM(B2:B9)'  # Dynamic calculation
```

## Workflow

1. Choose tool: pandas for data, openpyxl for formulas/formatting
2. Create/Load workbook
3. Modify: Add data, formulas, formatting
4. Save
5. Recalculate formulas (if using formulas)
6. Verify for errors
