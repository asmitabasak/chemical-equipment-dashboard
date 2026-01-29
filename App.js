import React, { useState } from 'react';
import axios from 'axios';
import { Line, Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend } from 'chart.js';

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend);

function App() {
  const [data, setData] = useState([]);
  const [stats, setStats] = useState({ total: 0, avgTemp: 0, maxPres: 0 });

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
      // Connect to your Django Backend
      const res = await axios.post('http://127.0.0.1:8000/api/upload/', formData);
      const equipment = res.data;
      
      setData(equipment);

      // Calculate Analytics
      const temps = equipment.map(i => parseFloat(i.Temperature) || 0);
      const pressures = equipment.map(i => parseFloat(i.Pressure) || 0);
      
      setStats({
        total: equipment.length,
        avgTemp: (temps.reduce((a, b) => a + b, 0) / equipment.length).toFixed(1),
        maxPres: Math.max(...pressures)
      });
    } catch (err) {
      console.error("Connection to Django failed", err);
    }
  };

  return (
    <div style={{ padding: '20px', backgroundColor: '#f8f9fc' }}>
      <header style={{ background: '#4e73df', color: 'white', padding: '20px', borderRadius: '10px' }}>
        <h1>Chemical Equipment Analytics</h1>
      </header>

      <div style={{ display: 'flex', gap: '20px', margin: '20px 0' }}>
        <div className="card"><h3>Total: {stats.total}</h3></div>
        <div className="card"><h3>Avg Temp: {stats.avgTemp}°C</h3></div>
        <div className="card"><h3>Max Pressure: {stats.maxPres} bar</h3></div>
      </div>

      <input type="file" onChange={handleFileUpload} accept=".csv" />

      <div style={{ width: '800px', margin: '20px auto' }}>
        <Line 
          data={{
            labels: data.map(i => i['Equipment Name']),
            datasets: [{ label: 'Pressure Levels', data: data.map(i => i.Pressure), borderColor: '#4e73df' }]
          }} 
        />
      </div>
    </div>
  );
}

export default App;
