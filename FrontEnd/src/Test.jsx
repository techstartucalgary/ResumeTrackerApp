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
            <div id="parent">
              
              <div style={{
              height: '850px', marginLeft: '10%', marginRight: '10%', marginTop: '150px', fontSize: '30px',
              }}
              >
                <h2 style={{"height": 200, "text-align":"center", "line-height": 400}}> Overview For:</h2>
                <h3 style={{"text-align":"center", "line-height": 100}}> {context.result.name}</h3>
                <p style={{"text-align":"center", "line-height": 100}}>
                  Total Score:
                  {' '}
                  {' '}
                  {context.result.totalScore}
                </p>

                <h4 style={{"text-align":"left", "line-height": 20}}> Education Review</h4>
                <p style={{fontSize: '30px', "text-align":"left", "line-height": 50}}>
                  Score:
                  {' '}
                  {' '}
                  {context.result.educationScore}
                </p>
                <p style={{fontSize: '10px', "text-align":"left", "line-height": 50}}>
                  {' '}
                  {' '}
                  {context.result.educationComments}
                </p>

                <h4 style={{"text-align":"right", "line-height": 20}}> Experience Review</h4>
                <p style={{"text-align":"right", "line-height": 50}}>
                  Score:
                  {' '}
                  {' '}
                  {context.result.experienceScore}
                </p>
                <p style={{fontSize: '10px', "text-align":"right", "line-height": 50}}>
                  {' '}
                  {' '}
                  {context.result.experienceComments}
                </p>
                <h4 style={{"text-align":"center", "line-height": 100}}> Formatting Review</h4>
                <p style={{"text-align":"center", "line-height": 0}}>
                  Score:
                  {' '}
                  {' '}
                  {context.result.formattingScore}
                </p>
                <p style={{fontSize: '10px', "text-align":"right", "line-height": 50}}>
                  {' '}
                  {' '}
                  {context.result.formattingComments}
                </p>

              </div>
            </div>
            
          );
        }}
      </ResumeContext.Consumer>
    </div>
  );
};




export default Test;
