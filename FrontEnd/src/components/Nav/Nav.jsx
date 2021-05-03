import { Link } from "react-router-dom";
import { Link as ScrollLink,  Element} from "react-scroll";
import "./Nav.scss";

const Nav = () => {
  return (
    <div className="nav-div">
      <Link className="nav-link" to="/">
        <h1 className="nav-title">Resume Rater</h1>
        <h3 className="nav-subtitle">By Tech Start UCalgary Team</h3>
      </Link>
      <ScrollLink
        activeClass="active"
        to="service"
        spy={true}
        smooth={true}
        duration={1000}
      >
      <button className="service-button">
        Our Service
      </button>
        </ScrollLink>
    </div>
  );
};

export default Nav;
