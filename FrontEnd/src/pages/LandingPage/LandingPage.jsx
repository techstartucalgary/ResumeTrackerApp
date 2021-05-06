import { AiOutlineCloudUpload } from 'react-icons/ai';
import { useHistory } from 'react-router-dom';
import React, { useContext } from 'react';
import ResumeSearch from '../../assets/ResumeSearch.svg';
import Underline from '../../assets/Underline.svg';
import ResumeContext from '../../contexts/ResumeContext';
import Balloons from '../../assets/Balloons.svg';
import Nav from '../../components/Nav/Nav';
import Footer from '../../components/Footer/Footer';
import ComputerSearch from '../../assets/ComputerSearch.svg';
import Person from '../../assets/Person.svg';
import './LandingPage.scss';

const LandingPage = () => {
  const history = useHistory();
  const { requestResults } = useContext(ResumeContext);

  return (
    <div>
      <Nav />
      <div className="main-div">
        <div className="upload-div">
          <div className="upload-left">
            <h1 className="upload-title">We make your resume stand out</h1>
            <img className="underline-image" src={Underline} alt="" />
            <p className="intro-text">
              We empower our users with the latest AI technology to rate their
              resumes and make sure they stand out from everyone else. Try
              scanning your resume now for free!
              <br />
              <br />
              For best performance on our service and companies Applicant Tracking System,
              please make sure that your resume has the format of a scannable resume.
              Some of the more important tips are avoiding horizontal and vertical lines
              and avoiding using special characters and bullet points. For more
              information on how to create a scannable resume, please visit
              &nbsp;
              <a href="https://www.careerchoiceguide.com/scannable-resume.html" target="_blank" rel="noreferrer">this website</a>
              .
            </p>

          </div>
          <img
            className="resume-search-image"
            src={ResumeSearch}
            alt="magnifying glass scanning a resume document"
          />
        </div>
        <div className="upload-file">
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
      <div name="service" className="service-div">
        <h1 className="service-title">Why use our service?</h1>
        <div className="upper-div">
          <img
            className="computer-search-image"
            src={ComputerSearch}
            alt="computer scanning a resume document"
          />
          <p className="ATS-text">
            Companies receive thousands of applications for each of their advertised positions.
            Not all of the resumes sent will be looked at by hiring managers; instead,
            companies use an Applicant Tracking System (ATS),
            which scans all resumes and then decides if your resume is worth being passed
            on to a recruiter.
            Some of them simply search for keywords while organizing candidates&apos;
            documents, making them searchable.
            Other ones use artificial intelligence for an even deeper analysis.
            These artificial intelligence models analyze
            past choices of the company to learn about the characteristics of desired employees.
            Even though each organization&apos;s
            selected employees are different according to its culture and values,
            all organizations have standard features that
            they look for in a candidate.
          </p>
        </div>
        <div>
          <p className="our-text">
            Our system ensures that you get through the Applicant Tracking
            System using AI&apos;s power and gives you the chance to have your
            resume checked by a recruiter.
            You can then get the chance to land that interview and your dream job. All free,
            with just one click!
          </p>
        </div>
        <div className="end-illustration">
          <img
            className="balloons-image"
            src={Balloons}
            alt="balloons"
          />
          <img
            className="person-image"
            src={Person}
            alt="person partying"
          />
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default LandingPage;
