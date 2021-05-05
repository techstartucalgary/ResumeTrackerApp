import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import PropTypes from 'prop-types';
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
            <Page key={i} pageNumber={i + 1} style={{ width: '300px', orientation: 'portrait' }} />
            {i !== (numberPages - 1) && (<br />)}
          </div>
        ))}
      </Document>
    </div>
  );
};

PDFDocument.propTypes = {
  inputFile: PropTypes.shape({
    lastModified: PropTypes.number,
    name: PropTypes.string,
    size: PropTypes.number,
    type: PropTypes.string,
    webkitRelativePath: PropTypes.string,
  }).isRequired,
};

export default PDFDocument;
