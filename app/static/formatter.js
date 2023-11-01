function getColour(data, value) {
  // Calculate the minimum and maximum values in the dataset
  const minValue = Math.min(...data);
  const maxValue = Math.max(...data);

  // Normalize the input value to a range between 0 and 1
  const normalizedValue = (value - minValue) / (maxValue - minValue);

  // Calculate the hue value (from green to red)
  const hue = normalizedValue * 120; // 0° is green, 120° is red

  // Set the saturation and lightness values for a soft and nice color
  const saturation = 100; // Adjust as needed
  const lightness = 68;  // Adjust as needed

  // Convert HSL to RGB
  const rgbColor = `hsl(${hue}, ${saturation}%, ${lightness}%)`;

  return rgbColor;
}