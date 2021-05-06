/* eslint-disable */
import axios from 'axios';
import React, { useCallback, useState, useEffect } from 'react';

export const ResumeContext = React.createContext({
  result: null,
  loading: false,
  formData: null,
  requestResults: () => {},
});

export const ResumeProvider = ({ children }) => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState(null);

  const requestResults = (value) => {
    setLoading(true);
    setFormData(value);
  };

  const requestData = useCallback(async () => {
    await axios
      .post('http://127.0.0.1:8000/wel', formData)
      .then((res) => {
        setResult({
          totalScore: res.data.totalScore,
          educationScore: res.data.educationScore,
          educationComments: res.data.educationComments,
          experienceScore: res.data.experienceScore,
          experienceComments: res.data.experienceComments,
          formattingScore: res.data.formattingScore,
          formattingComments: res.data.formattingComments,
          name: res.data.name,
          details: res.data.details,
        });
      })
      .catch((err) => {
        setLoading(false);
        console.log(err);
      })
      .finally(() => setLoading(false));
  }, [formData]);

  useEffect(() => {
    if (formData !== null) {
      setTimeout(() => { requestData(); }, 3000);
      // requestData();
    }
  }, [formData]);

  const context = {
    result,
    loading,
    formData,
    requestResults,
  };

  return (
    <ResumeContext.Provider value={context}>
      {typeof children === 'function' ? children(context) : children}
    </ResumeContext.Provider>
  );
};

export default ResumeContext;
