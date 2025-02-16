import React from 'react';
import './styles.css';

const StyledButton = ({ type = 'button', onClick, children, ...props }) => {
  return (
    <button type={type} onClick={onClick} className="styled-button" {...props}>
      {children}
    </button>
  );
};

export default StyledButton;
