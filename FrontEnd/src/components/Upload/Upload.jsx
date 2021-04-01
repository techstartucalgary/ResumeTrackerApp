import ResumeSearch from "../../assets/ResumeSearch.svg";
import Underline from "../../assets/Underline.svg";
import { AiOutlineCloudUpload } from "react-icons/ai";
import { useHistory } from "react-router-dom";
import ResumeContext from "../../contexts/ResumeContext";
import "./Upload.scss";
import React, { useContext, useEffect } from "react";

const Upload = () => {
  const history = useHistory();
  const { loading, requestResults } = useContext(ResumeContext);

  useEffect(() => {
    if (loading) {
      history.push("/results");
    }
  }, [loading, history]);

  return (
    <div className="main-div">
      <div className="upload-div">
        <div className="upload-left">
          <h1 className="upload-title">We make your resume stand out</h1>
          <img className="underline-image" src={Underline} alt="" />
          <p className="intro-text">
            We empower our users with the latest AI technology to rate their
            resumes and make sure they stand out from everyone else. Try
            scanning your resume now for free!
          </p>
        </div>
        <img
          className="resume-search-image"
          src={ResumeSearch}
          alt="magnifying glass scanning a resume document"
        />
      </div>
      <div className="upload-file">
        <ResumeContext.Consumer>
          {() => (
            <label htmlFor="input-file">
              <i>
                <AiOutlineCloudUpload />
              </i>
              <p className="button-text">Upload Your Resume</p>
              <input
                id="input-file"
                type="file"
                onChange={(e) => {
                  e.preventDefault();
                  const formData = new FormData();
                  formData.append(
                    "myFile",
                    e.target.files[0],
                    e.target.files[0].name
                  );
                  requestResults(formData);
                }}
                hidden
              />
            </label>
          )}
        </ResumeContext.Consumer>
      </div>
      <div className="temp"></div>
    </div>
  );
};
export default Upload;
