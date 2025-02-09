// Wait for the DOM to load before running our script
document.addEventListener('DOMContentLoaded', () => {
    // Grab all shape buttons, and the containers for our form and result.
    const shapeButtons = document.querySelectorAll('.shape_button');
    const formContainer = document.getElementById('area_form');
    const resultContainer = document.getElementById('area_result');
  
    // Function that returns the HTML for the form based on the selected shape.
    function generateForm(shape) {
      let formHtml = '';
      switch (shape) {
        case 'circle':
          formHtml = `
            <div>
              <label for="radius">Radius:</label>
              <input type="number" id="radius" name="radius" required step="any" min="0">
            </div>
            <button type="button" id="calcAreaBtn">Calculate Area</button>
          `;
          break;
        case 'rectangle':
          formHtml = `
            <div>
              <label for="width">Width:</label>
              <input type="number" id="width" name="width" required step="any" min="0">
            </div>
            <div>
              <label for="height">Height:</label>
              <input type="number" id="height" name="height" required step="any" min="0">
            </div>
            <button type="button" id="calcAreaBtn">Calculate Area</button>
          `;
          break;
        case 'square':
          formHtml = `
            <div>
              <label for="side">Side:</label>
              <input type="number" id="side" name="side" required step="any" min="0">
            </div>
            <button type="button" id="calcAreaBtn">Calculate Area</button>
          `;
          break;
        case 'triangle':
          formHtml = `
            <div>
              <label for="base">Base:</label>
              <input type="number" id="base" name="base" required step="any" min="0">
            </div>
            <div>
              <label for="height">Height:</label>
              <input type="number" id="height" name="height" required step="any" min="0">
            </div>
            <button type="button" id="calcAreaBtn">Calculate Area</button>
          `;
          break;
        default:
          formHtml = '';
      }
      return formHtml;
    }
  
    // Loop through each shape button to attach a click event listener.
    shapeButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Clear any previous form or result.
        formContainer.innerHTML = '';
        resultContainer.innerHTML = '';
  
        // Get the shape type from the button's value.
        const shape = button.value;
  
        // Insert the appropriate form into the area_form container.
        formContainer.innerHTML = generateForm(shape);
  
        // Attach an event listener to the newly created Calculate Area button.
        const calcAreaBtn = document.getElementById('calcAreaBtn');
        calcAreaBtn.addEventListener('click', () => {
          let area = 0; // To store our calculated area.
  
          // Calculate area based on the shape selected.
          if (shape === 'circle') {
            const radius = parseFloat(document.getElementById('radius').value);
            if (isNaN(radius) || radius <= 0) {
              resultContainer.innerHTML = '<p>Please enter a valid radius.</p>';
              return;
            }
            area = Math.PI * Math.pow(radius, 2);
          } else if (shape === 'rectangle') {
            const width = parseFloat(document.getElementById('width').value);
            const height = parseFloat(document.getElementById('height').value);
            if (isNaN(width) || width <= 0 || isNaN(height) || height <= 0) {
              resultContainer.innerHTML = '<p>Please enter valid dimensions.</p>';
              return;
            }
            area = width * height;
          } else if (shape === 'square') {
            const side = parseFloat(document.getElementById('side').value);
            if (isNaN(side) || side <= 0) {
              resultContainer.innerHTML = '<p>Please enter a valid side length.</p>';
              return;
            }
            area = Math.pow(side, 2);
          } else if (shape === 'triangle') {
            const base = parseFloat(document.getElementById('base').value);
            const height = parseFloat(document.getElementById('height').value);
            if (isNaN(base) || base <= 0 || isNaN(height) || height <= 0) {
              resultContainer.innerHTML = '<p>Please enter valid dimensions.</p>';
              return;
            }
            area = 0.5 * base * height;
          }
  
          // Display the calculated area (rounded to 2 decimal places).
          resultContainer.innerHTML = `<p>Area: ${area.toFixed(2)}</p>`;
        });
      });
    });
  });
  