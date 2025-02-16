import { useState } from 'react'
import React from 'react';
import './styles.css';

// Reusable TextInput component
export const TextInput = ({ type = 'text', id, name, value, onChange, ...props }) => {
  return (
    <input
      type={type}
      id={id}
      name={name}
      value={value}
      onChange={onChange}
      className="text-input"
      {...props}
    />
  );
};

// LabeledInput nests a label with the TextInput component
const LabeledInput = ({ label, type, id, name, value, onChange, ...props }) => {
  return (
    <div className="labeled-input">
      <label htmlFor={id} className="input-label">
        {label}
      </label>
      <TextInput type={type} id={id} name={name} value={value} onChange={onChange} {...props} />
    </div>
  );
};

export default LabeledInput;
