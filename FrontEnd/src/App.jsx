
import axios from 'axios';

import React,{Component} from 'react';

import Nav from './components/Nav/Nav';
import Footer from './components/Footer/Footer';

import { BrowserRouter } from 'react-router-dom'

class App extends Component {

    state = {

      // Initially, no file is selected
      selectedFile: null,
      totalScore: null,
      educationScore: null,
      educationComments: null,
      experienceScore: null,
      experienceComments: null,
      formattingScore: null,
      formattingComments: null,
      name: null,
      detail: null,
    };

    // On file select (from the pop up)
    onFileChange = event => {

      // Update the state
      this.setState({selectedFile: event.target.files[0]
      	});



    };

    // On file upload (click the upload button)
     onFileUpload = () => {

      // Create an object of formData
      const formData = new FormData();

      // Update the formData object
      formData.append(
        "myFile",
        this.state.selectedFile,
        this.state.selectedFile.name
      );

      // Details of the uploaded file
      console.log(this.state.selectedFile);

      // Request made to the backend api
      // Send formData object
       axios.post("http://127.0.0.1:8000/wel", formData)
        .then(res=> {
          this.setState({totalScore: res.data.totalScore,
          educationScore: res.data.educationScore,
          educationComments: res.data.educationComments,
          experienceScore: res.data.experienceScore,
          experienceComments: res.data.experienceComments,
          formattingScore: res.data.formattingScore,
          formattingComments: res.data.formattingComments,
          name: res.data.name,
          details: res.data.details
          });
        })
        .catch(function (error) {
          console.log(error);
        });
       };



    // File content to be displayed after
    // file upload is complete
    fileData = () => {

      if (this.state.totalScore) {

        return (
          <div>
            <h2>File Details:</h2>


<p>
			   Total Score: {" "}
			   {this.state.totalScore}
			</p>

<p>
			   Education Score: {" "}
			   {this.state.educationScore}
			</p>

<p>
			   Education Comments: {" "}
			   {this.state.educationComments}
			</p>

<p>
			   Experience Score: {" "}
			   {this.state.experienceScore}
			</p>

<p>
			   Experience Comments: {" "}
			   {this.state.experienceComments}
			</p>

<p>
			   Formatting Score: {" "}
			   {this.state.formattingScore}
			</p>

<p>
			   Formatting Comments: {" "}
			   {this.state.formattingComments}
			</p>

<p>
			   Name: {" "}
			   {this.state.name}
			</p>

<p>
			   Details: {" "}
			   {this.state.details}
			</p>

          </div>
        );
      } else {
        return (
          <div>
            <br />
            <h4>Select PDF file to Upload</h4>
          </div>
        );
      }
    };

    render() {

      return (
        <div>
        <BrowserRouter>
        <Nav />
        </BrowserRouter>
          {/*  <h1>
              Resume Tracker Basic Front End
            </h1>
            <h3>
              File Upload
            </h3>
            <div>
                <input type="file" onChange={this.onFileChange} />
                <button onClick={this.onFileUpload}>
                  Upload!
                </button>
            </div>
          {this.fileData()}*/}
          <Footer />
        </div>
      );
    }
  }

  export default App;
