import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { AiOutlineCloudUpload } from 'react-icons/ai';
import ResumeContext from '../../contexts/ResumeContext';
import './UploadBox.scss';

const UploadBox = () => {
  const history = useHistory();
  const { requestResults } = useContext(ResumeContext);
  const [style, setStyle] = useState(null);

  const handleDragOver = (e) => {
    e.preventDefault();
    setStyle({
      opacity: '1',
      padding: '10px',
      backgroundColor: 'white',
    });
  };

  const handleDragEnter = (e) => {
    e.preventDefault();
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setStyle(null);
  };

  const handleFileDrop = (e) => {
    e.preventDefault();
    const sentFormData = new FormData();
    sentFormData.append(
      'myFile',
      e.dataTransfer.files[0],
      e.dataTransfer.files[0].name,
    );
    history.push('/results');
    requestResults(sentFormData);
  };

  return (
    <div
      className="upload-box-container"
      onDragOver={handleDragOver}
      onDragEnter={handleDragEnter}
      onDragLeave={handleDragLeave}
      onDrop={handleFileDrop}
      style={style}
    >
      <div className="upload-box-inner">
        <label htmlFor="input-file">
          <i>
            {!style && <AiOutlineCloudUpload />}
          </i>
          {!style ? <h4 className="button-text">Drop or select your resume</h4> : <h2 className="drop-message">Drop Resume!</h2>}
          <input
            id="input-file"
            type="file"
            onChange={(e) => {
              e.preventDefault();
              const sentFormData = new FormData();
              sentFormData.append(
                'myFile',
                e.target.files[0],
                e.target.files[0].name,
              );
              history.push('/results');
              requestResults(sentFormData);
            }}
            hidden
          />
        </label>
      </div>
    </div>
  );
};

export default UploadBox;
