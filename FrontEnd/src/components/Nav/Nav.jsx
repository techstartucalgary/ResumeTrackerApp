import { Link } from 'react-router-dom';
import { Link as scrollLink } from "react-scroll";
import './Nav.scss';

const Nav = () => {
  return (
    <div className="nav-div">
      <Link className='nav-link' to='/'>
        <h1 className="nav-title">Resume Rater</h1>
        <h3 className="nav-subtitle">By Tech Start UCalgary Team</h3>
      </Link>
      <button className="service-button">
      <scrollLink
      activeClass="active"
      to=""
      spy={true}
      smooth={true}
      offset={-70}
      duration={500}/>
      Our Service</button>
    </div>
  );
};

export default Nav;
