import React from 'react';
import './Dashboard.css'
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import Drawer from '@mui/material/Drawer';
import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import HomeOutlinedIcon from '@mui/icons-material/HomeOutlined';
import PeopleAltOutlinedIcon from '@mui/icons-material/PeopleAltOutlined';
import NotificationsOutlinedIcon from '@mui/icons-material/NotificationsOutlined';
import FolderOutlinedIcon from '@mui/icons-material/FolderOutlined';
import InsertDriveFileOutlinedIcon from '@mui/icons-material/InsertDriveFileOutlined';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import HelpOutlineOutlinedIcon from '@mui/icons-material/HelpOutlineOutlined';
import { ListItemIcon, Typography } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const { palette } = createTheme();
const { augmentColor } = palette;
const createColor = (mainColor) => augmentColor({ color: { main: mainColor } });

const themeLight = createTheme({
    
    palette: {
        retyrn_blue: createColor('#4ca7da'),
        background: {
            default: "#F2F2F2"
        }
    }
});
const drawerWidth = 240;

export default function Dashboard(props) {
  const { window } = props;
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

//   The drawer lists some of the pages that the user can access
  const drawer = (
    <div>
      <Toolbar>
        <Typography
            variant='h6'
            color='#000000'
            
        >
            Name
        </Typography>
            
        <Typography
            variant='body2'
            color='#000000'
        >
            Role
        </Typography>
      </Toolbar>
      <Divider />
      {/*  Each of the items listed should be a component. For example, accounts should
      display the list of accounts */}
      <List>
        <ListItem disablePadding>
            <ListItemButton>
                <ListItemIcon><HomeOutlinedIcon></HomeOutlinedIcon></ListItemIcon>
                <ListItemText>Home</ListItemText>
            </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
            <ListItemButton>
                <ListItemIcon><PeopleAltOutlinedIcon></PeopleAltOutlinedIcon></ListItemIcon>
                <ListItemText>Accounts</ListItemText>
            </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
            <ListItemButton>
                <ListItemIcon><NotificationsOutlinedIcon></NotificationsOutlinedIcon></ListItemIcon>
                <ListItemText>Notifications</ListItemText>
            </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
            <ListItemButton>
                <ListItemIcon><InsertDriveFileOutlinedIcon></InsertDriveFileOutlinedIcon></ListItemIcon>
                <ListItemText>Claims</ListItemText>
            </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
            <ListItemButton>
                <ListItemIcon><FolderOutlinedIcon></FolderOutlinedIcon></ListItemIcon>
                <ListItemText>Documents</ListItemText>
            </ListItemButton>
        </ListItem>
      </List>
      <Divider />
      <List>
      <ListItem disablePadding>
            <ListItemButton>
                <ListItemIcon><PeopleAltOutlinedIcon></PeopleAltOutlinedIcon></ListItemIcon>
                <ListItemText>Manage Permissions</ListItemText>
            </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
            <ListItemButton>
                <ListItemIcon><SettingsOutlinedIcon></SettingsOutlinedIcon></ListItemIcon>
                <ListItemText>Settings</ListItemText>
            </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
            <ListItemButton>
                <ListItemIcon><HelpOutlineOutlinedIcon></HelpOutlineOutlinedIcon></ListItemIcon>
                <ListItemText>Help</ListItemText>
            </ListItemButton>
        </ListItem>
      </List>
    </div>
  );

  const container = window !== undefined ? () => window().document.body : undefined;

  return (
    <ThemeProvider theme={themeLight}>
        <Box sx={{ display: 'flex', }}>
        <CssBaseline />
        <AppBar
            elevation={0}
            position="fixed"
            sx={{
            width: { sm: `calc(100% - ${drawerWidth}px)` },
            ml: { sm: `${drawerWidth}px` },
            backgroundColor:'#FFFFFF',
            color: '#080D1C'
            }}
        >  
            
            <Toolbar>
                {/* This is the menu icon. Once it is clicked, it will 
                toggle handleDrawerToggle to which will open the drawer */}
            <IconButton
                color="inherit"
                aria-label="open drawer"
                edge="start"
                onClick={handleDrawerToggle}
                sx={{ mr: 2, display: { sm: 'none' } }}
            >
                <MenuIcon />
            </IconButton>
            <Typography
                variant='h4'
                color='#4CA7DA'
            >
                Retyrn
            </Typography>
            </Toolbar>
            <Divider />
        </AppBar>
        <Box
            component="nav"
            sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
            aria-label="mailbox folders"
        >
            {/* When on mobile view, the drawer is closed unless the user clicks on the hamburger icon */}
            <Drawer
            container={container}
            variant="temporary"
            open={mobileOpen}
            onClose={handleDrawerToggle}
            ModalProps={{
                keepMounted: true, // Better open performance on mobile.
            }}
            sx={{
                display: { xs: 'block', sm: 'none' },
                '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
            }}
            >
            {drawer}
            </Drawer>
            {/* When on Desktop view, the drawer is always shown. */}
            <Drawer
            variant="permanent"
            sx={{
                display: { xs: 'none', sm: 'block' },
                '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
            }}
            open
            >
            {drawer}
            </Drawer>
        </Box>

        {/* Main component to which displays whatever we want. */}
        <Box
            component="main"
            sx={{ flexGrow: 1, p: 3, width: { sm: `calc(100% - ${drawerWidth}px)` }}}
        >
            <Toolbar />
            {/* Under this toolbar is where want to display things */}
            <Typography>For example: Hi</Typography>
        </Box>
        </Box>
    </ThemeProvider>
  );
}
