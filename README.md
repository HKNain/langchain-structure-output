# Structured Output Examples

This folder contains small Python examples that demonstrate different ways to
represent, validate, and generate structured data:

- Python `TypedDict`
- Pydantic models
- LangChain structured output
- Gemini JSON Schema responses

## Files

| File | Description |
| --- | --- |
| [`typed_dict.py`](./typed_dict.py) | Defines a `Person` `TypedDict` and creates a typed dictionary value. |
| [`pydantic_op.py`](./pydantic_op.py) | Defines a `Student` Pydantic model and validates input data at runtime. |
| [`langchain_op.py`](./langchain_op.py) | Uses LangChain's `with_structured_output` with a `TypedDict` review schema. |
| [`json_op.py`](./json_op.py) | Requests a JSON response from Gemini using an external JSON Schema, then validates it with Pydantic. |
| [`student_schema.json`](./student_schema.json) | JSON Schema for a student with a name, age, and list of skills. |
| [`requirements.txt`](./requirements.txt) | Python dependencies used by the examples. |

## Requirements

- Python 3.9 or newer
- A Gemini API key for [`langchain_op.py`](./langchain_op.py) and
  [`json_op.py`](./json_op.py)

## Setup

From this directory, create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in this directory:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
```

Both API-backed examples load this variable with `python-dotenv`. Keep the
`.env` file private; it is excluded by the local `.gitignore`.

## Running the examples

```powershell
python typed_dict.py
python pydantic_op.py
python langchain_op.py
python json_op.py
```

The first two scripts run locally. The LangChain and Gemini examples send
requests to Gemini and require a valid API key and network access.

## What the examples demonstrate

### `TypedDict`

`TypedDict` describes the expected keys and value types for static type
checkers. It does not perform runtime validation by itself.

### Pydantic

Pydantic models validate and parse data at runtime. The
[`pydantic_op.py`](./pydantic_op.py) example shows a `Student` model being
constructed from a dictionary.

### LangChain structured output

[`langchain_op.py`](./langchain_op.py) supplies a `Review` schema to
`with_structured_output`, asking the model to return a result with `summary`
and `sentiment` fields.

### Gemini JSON Schema

[`json_op.py`](./json_op.py) uses [`student_schema.json`](./student_schema.json)
to constrain Gemini's response to JSON, then validates the returned JSON with a
Pydantic `Student` model.