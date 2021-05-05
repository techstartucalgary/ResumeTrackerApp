import { useHistory } from 'react-router-dom';
import React, { useContext } from 'react';
import Lottie from 'react-lottie';
import PDFDocument from '../../components/PDFDocument/PDFDocument';
import Nav from '../../components/Nav/Nav';
import Footer from '../../components/Footer/Footer';
import UploadBox from '../../components/UploadBox/UploadBox';
import ScoreBreakDown from '../../components/ScoreBreakDown/ScoreBreakDown';
import ResumeContext from '../../contexts/ResumeContext';
import Searching from '../../assets/Searching.json';
import './ResultsPage.scss';

const Test = () => {
  const history = useHistory();
  const options = {
    animationData: Searching,
  };
  const {
    formData, result, loading,
  } = useContext(ResumeContext);
  const savedFormData = formData;
  const showResult = result && !loading;

  if (result == null && !loading) {
    history.push('/');
    return null;
  }

  return (
    <div>
      {loading && (
      <div id="searching-animation" style={{ minHeigth: '800px', marginTop: '60px' }}>
        <Lottie
          options={options}
          height={600}
          width={600}
        />
        <h1 style={{ marginBottom: '100px', marginLeft: '40%' }}>
          Scanning Your Resume .......
        </h1>
      </div>
      )}

      {showResult
      && (
        <div>
          <Nav />
          <div className="results-upper">
            <PDFDocument inputFile={savedFormData.get('myFile')} />
            <div className="results-score">
              <h1 className="total-score">
                Total Score:&nbsp;
                {result.totalScore}
              </h1>
              <ScoreBreakDown scoreCategory="Education Score" score={result.educationScore} comments={result.educationComments} />
              <ScoreBreakDown scoreCategory="Experience Score" score={result.experienceScore} comments={result.experienceComments} />
              <ScoreBreakDown scoreCategory="Formatting Score" score={result.formattingScore} comments={result.formattingComments} />
            </div>
          </div>
          <div>
            <UploadBox />
          </div>
          <Footer />
        </div>
      )}
    </div>
  );
};

export default Test;
