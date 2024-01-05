# Health AI

## Description
A simple model fine tuning pipe line for text generation using GPT-2

## Installation

### Prerequisites
- Python 3.11
- pipenv
- pytorch


If you don't have pipenv installed, you can install it using pip:

```bash
pip install pipenv
```

```bash
git clone https://github.com/MehdiZare/healthai
cd healthai
pipenv install
```
## Environment Variables
You need to set the `API_KEY` to the API key for accessing mediastack. It can be saved in a `.env` file in the root of the project.


## Usage

Use training notebook to train the model and then use the inference notebook to generate text.

Model weights are too large to be saved in the repo. You can download the weight folder from 
[here](https://drive.google.com/drive/folders/1TrO_08gv6_NVbE9pZxeQ__rdnUxYUOlq?usp=drive_link) and put it in the root folder.