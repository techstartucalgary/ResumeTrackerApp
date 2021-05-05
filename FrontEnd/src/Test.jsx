import { useHistory } from 'react-router-dom';
import React from 'react';
import Lottie from 'react-lottie';
import ResumeContext from './contexts/ResumeContext';
import Searching from './assets/Searching.json';

const Test = () => {
  const history = useHistory();
  // const { loading } = useContext(ResumeContext);
  const options = {
    animationData: Searching,
  };
  /* useEffect(() => {
      lottie.loadAnimation({
      container: document.querySelector("#searching-animation"),
      animationData: Searching,
    });
  }, []); */
  return (
    <div>
      <ResumeContext.Consumer>
        {(context) => {
          if (context.result == null && !context.loading) {
            history.push('/');
            return null;
          } if (context.results == null && context.loading) {
            return (
              <div id="searching-animation" style={{ minHeigth: '800px', marginTop: '60px' }}>
                <Lottie
                  options={options}
                  height={600}
                  width={600}
                />
                <h1 style={{ marginBottom: '100px', marginLeft: '40%' }}>Scanning Your Resume .......</h1>
              </div>
            );
          }
          // lottie.setVisibility(false);
          return (
            <div style={{
              height: '650px', marginLeft: '35%', marginTop: '100px', fontSize: '30px',
            }}
            >
              <h2>File Details:</h2>

              <p>
                Total Score:
                {' '}
                {' '}
                {context.result.totalScore}
              </p>

              <p>
                Education Score:
                {' '}
                {' '}
                {context.result.educationScore}
              </p>

              <p>
                Education Comments:
                {' '}
                {' '}
                {context.result.educationComments}
              </p>

              <p>
                Experience Score:
                {' '}
                {' '}
                {context.result.experienceScore}
              </p>

              <p>
                Experience Comments:
                {' '}
                {' '}
                {context.result.experienceComments}
              </p>

              <p>
                Formatting Score:
                {' '}
                {' '}
                {context.result.formattingScore}
              </p>

              <p>
                Formatting Comments:
                {' '}
                {' '}
                {context.result.formattingComments}
              </p>

              <p>
                Name:
                {' '}
                {' '}
                {context.result.name}
              </p>

              <p>
                Details:
                {' '}
                {' '}
                {context.result.details}
              </p>

            </div>
          );
        }}
      </ResumeContext.Consumer>
    </div>
  );
};

export default Test;
