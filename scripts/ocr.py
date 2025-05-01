def main():
    from doctr.io import DocumentFile
    from doctr.models import ocr_predictor

    model = ocr_predictor(pretrained=True)
    # PDF
    doc = DocumentFile.from_images("./scripts/dummy/pizzeria.jpeg")
    # Analyze
    result = model(doc)
    print(result)
    result.show()


if __name__ == "__main__":
    main()
