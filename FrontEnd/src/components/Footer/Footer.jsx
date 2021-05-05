import React from 'react';
import {
  AiFillInstagram,
  AiFillFacebook,
  AiFillLinkedin,
} from 'react-icons/ai';

import './Footer.scss';

const Footer = () => (
  <div className="footer-div">
    <div className="footer-contact-info">
      <AiFillFacebook
        onClick={(e) => {
          e.preventDefault();
          window.open(
            'https://www.facebook.com/Tech-Start-UCalgary',
            '_blank',
          );
        }}
      />
      <AiFillInstagram
        onClick={(e) => {
          e.preventDefault();
          window.open(
            'https://www.instagram.com/techstartucalgary/',
            '_blank',
          );
        }}
      />
      <AiFillLinkedin
        onClick={(e) => {
          e.preventDefault();
          window.open(
            'https://www.linkedin.com/company/tech-start-ucalgary/',
            '_blank',
          );
        }}
      />
    </div>
  </div>
);

export default Footer;
