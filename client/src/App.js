import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [stockData, setStockData] = useState([]);
  const [editedData, setEditedData] = useState({});

  // Fetch stock data from Django backend
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/stock-data/")
      .then((response) => {
        setStockData(response.data);
      })
      .catch((error) => {
        alert("Error fetching stock data");
      });
  }, []);

  // Handle input change in editable table
  const handleInputChange = (index, key, value) => {
    const updatedData = [...stockData];
    updatedData[index][key] = value;
    setStockData(updatedData);

    // Store changes in editedData
    setEditedData((prev) => ({
      ...prev,
      [index]: { ...prev[index], [key]: value },
    }));
  };

  // Send updated data to the backend
  const handleSave = (index) => {
    const updatedRow = { ...stockData[index] }; // Get updated row data

    axios
      .put(
        `http://127.0.0.1:8000/api/update-stock/${updatedRow.id}/`,
        updatedRow
      )
      .then(() => {
        alert("Data updated successfully!");
      })
      .catch(() => {
        alert("Error updating data");
      });
  };

  return (
    <div>
      <h1>Stock Market Data (Editable)</h1>
      <table border="1">
        <thead>
          <tr>
            {stockData.length > 0 &&
              Object.keys(stockData[0]).map((key) => <th key={key}>{key}</th>)}
            <th>Actions</th> {/* Add Actions column for Save button */}
          </tr>
        </thead>
        <tbody>
          {stockData.map((row, index) => (
            <tr key={index}>
              {Object.keys(row).map((key) => (
                <td key={key}>
                  <input
                    type="text"
                    value={row[key]}
                    onChange={(e) =>
                      handleInputChange(index, key, e.target.value)
                    }
                  />
                </td>
              ))}
              <td>
                <button onClick={() => handleSave(index)}>Save</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
