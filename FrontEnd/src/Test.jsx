import ResumeContext from './contexts/ResumeContext';
import { useHistory } from 'react-router-dom';

const Test = () => {
  const history = useHistory();
  return(
    <div>
    <ResumeContext.Consumer>
             {(context) => {
               if(context.result == null){
                 history.push('/');
                 return;
               }
            return (
              <div>
                <h2>File Details:</h2>


    <p>
    			   Total Score: {" "}
    			   {context.result.totalScore}
    			</p>

    <p>
    			   Education Score: {" "}
    			   {context.result.educationScore}
    			</p>

    <p>
    			   Education Comments: {" "}
    			   {context.result.educationComments}
    			</p>

    <p>
    			   Experience Score: {" "}
    			   {context.result.experienceScore}
    			</p>

    <p>
    			   Experience Comments: {" "}
    			   {context.result.experienceComments}
    			</p>

    <p>
    			   Formatting Score: {" "}
    			   {context.result.formattingScore}
    			</p>

    <p>
    			   Formatting Comments: {" "}
    			   {context.result.formattingComments}
    			</p>

    <p>
    			   Name: {" "}
    			   {context.result.name}
    			</p>

    <p>
    			   Details: {" "}
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
