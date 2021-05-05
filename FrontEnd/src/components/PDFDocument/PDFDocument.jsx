/* eslint-disable */
import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import './PDFDocument.scss';

const PDFDocument = ({ inputFile }) => {
  const [numberPages, setNumberPages] = useState(null);
  const [file, setFile] = useState(null);

  pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

  const onDocumentLoadSuccess = ({ numPages }) => {
    setNumberPages(numPages);
  };

  const reader = new FileReader();
  try {
    reader.readAsDataURL(inputFile);
  } catch (err) {
    console.log(err);
  }

  reader.onloadend = () => {
    console.log('reader result is: ', reader.result);
    setFile(reader.result);
  };

  return (
    <div className="pdf-container">
      <Document
        file={file}
        onLoadSuccess={onDocumentLoadSuccess}
      >
        {Array.from({ length: numberPages }, (v, i) => (
          <div>
            <Page size="A4" key={i} pageNumber={i + 1} style={{ width: '300px', orientation: 'portrait' }} />
            {i != (numberPages - 1) && (<br />)}
          </div>
        ))}
      </Document>
    </div>
  );
};

export default PDFDocument;
