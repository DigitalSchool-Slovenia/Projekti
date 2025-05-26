// Smooth Scrolling for Navigation Links
const links = document.querySelectorAll('nav ul li a');


// Tooltip functionality for <code> elements
const codeElements = document.querySelectorAll('code');

codeElements.forEach(element => {
  element.addEventListener('mouseover', function () {
    const tooltip = document.createElement('div');
    tooltip.classList.add('tooltip');
    tooltip.textContent = `This is an HTML tag: ${this.textContent}`;
    document.body.appendChild(tooltip);

    const rect = this.getBoundingClientRect();
    tooltip.style.left = `${rect.left + window.scrollX}px`;
    tooltip.style.top = `${rect.top + window.scrollY - 30}px`; // Position above the element

    // Remove tooltip on mouseout
    this.addEventListener('mouseout', () => {
      tooltip.remove();
    });
  });
});
