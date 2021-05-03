import React from 'react';
import { Link } from 'react-router-dom';
import { Link as ScrollLink } from 'react-scroll';
import './Nav.scss';

const Nav = () => (
  <div className="nav-div">
    <Link className="nav-link" to="/">
      <h1 className="nav-title">Resume Rater</h1>
      <h3 className="nav-subtitle">By Tech Start UCalgary Team</h3>
    </Link>
    <ScrollLink
      activeClass="active"
      to="service"
      spy
      smooth
      duration={1000}
    >
      <button type="submit" className="service-button">
        Our Service
      </button>
    </ScrollLink>
  </div>
);

export default Nav;
