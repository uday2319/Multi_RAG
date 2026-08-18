from ingestion.figure_processor import extract_figures


pdf_path = "data/papers/research_paper.pdf"

figures = extract_figures(pdf_path)

print("Figures extracted:", len(figures))

for figure in figures:
    print("\n----------------")
    print("Page:", figure["page"])
    print("Figure:", figure["figure_id"])
    print("Path:", figure["path"])