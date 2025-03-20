# Instructions for Analyzing Papers with Claude.ai

Please ensure you have your web cookie from [Claude.ai](https://claude.ai/) and save it into the `.cookie` file before proceeding.

1. To download PDFs based on `cv-arxiv-daily-web.json`, execute:

```shell
python download_pdf.py
```

2. To convert `pdf` to `txt` or `markdown` format, run:

```shell
python parse_pdf.py
```

Notes: 

* You can choose either `raw_text` or `rich_markdown` format.
* `raw_text` is simple and retains only the text, while `rich_markdown` supports parsing tables, formulas, and references.
* We recommend using `rich_markdown` based on [Sciparser](https://github.com/davendw49/sciparser). However, it must be noted that installing `Sciparser` can be somewhat complicated, and you need to run a service using Docker, for example:
```docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.0```
* For details, you can refer to the [GROBID documentation](https://grobid.readthedocs.io/en/latest/Run-Grobid/).

3. To initiate the analysis process, run:

```shell
python analysis_papers.py
```

4. To generate a markdown file for the analysis, use:

```shell
python generating_paper_analysis.py
```


5. [Optional] To obtain insights on recent trends or ideas from the latest N papers, execute:

OpenAI API is not updated here.

```shell
python analysis_recent_trends.py
```

This project utilizes the [Claude2-PyAPI](https://github.com/wwwzhouhui/Claude2-PyAPI).


* Please note that due to updates in the Claude interface, the functionality of the provided code may vary over time.

* While this project is actively maintained, there may still be occasional bugs. We encourage users to proceed with caution and contribute improvements via pull requests.
