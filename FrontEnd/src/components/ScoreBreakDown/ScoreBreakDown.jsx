import React, { useState } from 'react';
import {
  BiRightArrow,
  BiDownArrow,
} from 'react-icons/bi';
import PropTypes from 'prop-types';
import './ScoreBreakDown.scss';

const ScoreBreakDown = ({ scoreCategory, score, comments }) => {
  const [open, setOpen] = useState(false);

  return (
    <div className="score-container">
      <div className="score-header">
        <h2>
          {scoreCategory}
          :
          {' '}
          {score}
        </h2>
        {open
          ? <BiDownArrow onClick={() => setOpen(!open)} />
          : <BiRightArrow onClick={() => setOpen(!open)} />}
      </div>
      {open && (
        <div className="score-dropdown">
          <h3>Comments: </h3>
          <br />
          <h4>{comments}</h4>
        </div>
      )}
    </div>
  );
};

ScoreBreakDown.propTypes = {
  scoreCategory: PropTypes.string.isRequired,
  score: PropTypes.number.isRequired,
  comments: PropTypes.string.isRequired,
};

export default ScoreBreakDown;
