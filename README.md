# 📝 Telugu FRA Document Synthesizer

Generate **realistic synthetic Telugu FRA (Forest Rights Act) documents** for AI and ML model training. This project helps create training datasets when real documents are scarce or confidential, ensuring your models can learn effectively from realistic data.

---

## 🚀 Features

- **Synthetic Document Generation**  
  Programmatically create FRA documents in Telugu that mimic real-world layouts and content.

- **Flexible Customization**  
  Adjust text fields, formatting, and structure to generate diverse document variations.

- **AI Training Ready**  
  Ideal for OCR, NLP, document parsing, or classification models.

- **Reference-Based Accuracy**  
  Synthesized documents are modeled after actual Telugu FRA and patta documents found online.

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/telugu-fra-synthesizer.git
cd telugu-fra-synthesizer
```

Install dependencies (Python example):

```bash
pip install -r requirements.txt
```

---

## ⚡ Usage

Generate a single FRA document:
```python
from fra_synthesizer import generate_document

generate_document(output_path="output/fra_doc_1.pdf")
```

Generate multiple documents:
```python
for i in range(10):
    generate_document(output_path=f"output/fra_doc_{i+1}.pdf")
```

---

## 📚 How It Works

- Uses **reference images** of Telugu FRA and patta documents.  
- Maps **document fields, fonts, and layout** to ensure realistic output.  
- Produces **PDFs or images** ready for AI training pipelines.

---

## 🎯 Use Cases

- Training **OCR models** for Telugu document recognition.  
- Building **NLP models** for content extraction or classification.  
- Experimenting with **document analysis pipelines** safely without sensitive data.

---

## 🖼️ Preview

Below are some examples of generated synthetic FRA documents:

[form_a_sample_1.docx](https://github.com/user-attachments/files/24127391/form_a_sample_1.docx)
[form_b_sample_1.docx](https://github.com/user-attachments/files/24127387/form_b_sample_1.docx)
[form_c_sample_1.docx](https://github.com/user-attachments/files/24127406/form_c_sample_1.docx)

<img width="491" height="648" alt="Screenshot 2025-12-12 182622" src="https://github.com/user-attachments/assets/69c6cab9-148a-4ed7-b2f2-edb4de1b3fa7" />

---

## 👥 Contributing

Contributions are welcome!  

1. Fork the repo  
2. Create a branch for your feature/fix  
3. Submit a pull request  

---

## 📄 License

MIT License

---

## 🔗 References

- Real Telugu FRA and patta documents available online.  
- Layouts and structure inspired from actual references to maximize realism.
