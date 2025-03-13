import React from 'react';
import { 
  AppBar, 
  Toolbar, 
  Typography, 
  Button, 
  Box 
} from '@mui/material';
import { useNavigate } from 'react-router-dom';

export const Navbar: React.FC = () => {
  const navigate = useNavigate();

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          DealerX
        </Typography>
        <Box sx={{ display: 'flex', gap: 2 }}>
          <Button color="inherit" onClick={() => navigate('/inventory')}>
            Inventory
          </Button>
          <Button color="inherit" onClick={() => navigate('/sales')}>
            Sales
          </Button>
          <Button color="inherit" onClick={() => navigate('/service')}>
            Service
          </Button>
          <Button color="inherit" onClick={() => navigate('/customers')}>
            Customers
          </Button>
          <Button color="inherit" onClick={() => navigate('/employees')}>
            Employees
          </Button>
          <Button color="inherit" onClick={() => navigate('/reports')}>
            Reports
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
}; 