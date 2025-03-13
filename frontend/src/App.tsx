import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Box } from '@mui/material';
import { Navbar } from './components/Navigation/Navbar';
import { VehicleList } from './components/Inventory/VehicleList';

// Placeholder components for other routes
const Sales = () => <div>Sales Page</div>;
const Service = () => <div>Service Page</div>;
const Customers = () => <div>Customers Page</div>;
const Employees = () => <div>Employees Page</div>;
const Reports = () => <div>Reports Page</div>;

function App() {
  return (
    <BrowserRouter>
      <Box sx={{ flexGrow: 1 }}>
        <Navbar />
        <Box sx={{ p: 3 }}>
          <Routes>
            <Route path="/" element={<Navigate to="/inventory" replace />} />
            <Route path="/inventory" element={<VehicleList />} />
            <Route path="/sales" element={<Sales />} />
            <Route path="/service" element={<Service />} />
            <Route path="/customers" element={<Customers />} />
            <Route path="/employees" element={<Employees />} />
            <Route path="/reports" element={<Reports />} />
          </Routes>
        </Box>
      </Box>
    </BrowserRouter>
  );
}

export default App; 