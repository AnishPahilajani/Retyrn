import React from "react";
import "./SideDrawer.css";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import Divider from "@mui/material/Divider";
import Drawer from "@mui/material/Drawer";
import IconButton from "@mui/material/IconButton";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import MenuIcon from "@mui/icons-material/Menu";
import Toolbar from "@mui/material/Toolbar";
import Avatar from "@mui/material/Avatar";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import PersonOutlineOutlinedIcon from "@mui/icons-material/PersonOutlineOutlined";
import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined";
import PeopleAltOutlinedIcon from "@mui/icons-material/PeopleAltOutlined";
import NotificationsOutlinedIcon from "@mui/icons-material/NotificationsOutlined";
import FolderOutlinedIcon from "@mui/icons-material/FolderOutlined";
import InsertDriveFileOutlinedIcon from "@mui/icons-material/InsertDriveFileOutlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";
import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";
import { ListItemIcon, Typography } from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";

const { palette } = createTheme();
const { augmentColor } = palette;
const createColor = (mainColor) => augmentColor({ color: { main: mainColor } });

const themeLight = createTheme({
  palette: {
    retyrn_blue: createColor("#4ca7da"),
    background: {
      default: "#F2F2F2",
    },
    font: "Roboto",
  },
});
const drawerWidth = 240;

export default function SideDrawer(props) {
  const { window } = props;
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const drawerTabs = [
    { name: "Home", icon: <HomeOutlinedIcon /> },
    { name: "Accounts", icon: <PersonOutlineOutlinedIcon /> },
    { name: "Notifications", icon: <NotificationsOutlinedIcon /> },
    { name: "Claims", icon: <InsertDriveFileOutlinedIcon /> },
    { name: "Documents", icon: <FolderOutlinedIcon /> },
  ];
  const drawerOtherTabs = [
    { name: "Manage Permissions", icon: <PeopleAltOutlinedIcon /> },
    { name: "Settings", icon: <SettingsOutlinedIcon /> },
    { name: "Help", icon: <HelpOutlineOutlinedIcon /> },
  ];

  //   The drawer lists some of the pages that the user can access
  const drawer = (
    <div>
      <Toolbar>
        {/* Displays the User's information */}
        <Card elevation={0} sx={{ width: 300 }}>
          <CardHeader
            avatar={<Avatar>N</Avatar>}
            action={
              <IconButton>
                <ArrowDropDownIcon></ArrowDropDownIcon>
              </IconButton>
            }
            title="Name"
            subheader="Role"
          />
        </Card>
      </Toolbar>
      <Divider />
      {/*  Each of the items listed should be a component. For example, accounts should
      display the list of accounts */}
      <List>
        {/* Traverses through drawerTabs and makes each object a list item button in the drawer */}
        {drawerTabs.map((item, index) => (
          <ListItemButton key={index}>
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.name} />
          </ListItemButton>
        ))}
      </List>
      <Divider />
      <List>
        {/* Traverses through drawerOtherTabs and makes each object a list item button in the drawer */}
        {drawerOtherTabs.map((item, index) => (
          <ListItemButton key={index}>
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.name} />
          </ListItemButton>
        ))}
      </List>
    </div>
  );

  const container =
    window !== undefined ? () => window().document.body : undefined;

  return (
    <ThemeProvider theme={themeLight}>
      <Box sx={{ display: "flex" }}>
        <CssBaseline />
        <AppBar
          elevation={0}
          position="fixed"
          sx={{
            width: { sm: `calc(100% - ${drawerWidth}px)` },
            ml: { sm: `${drawerWidth}px` },
            backgroundColor: "#FFFFFF",
            color: "#080D1C",
          }}
        >
          <Toolbar sx={{ height: 72 }}>
            {/* This is the menu icon. Once it is clicked, it will 
                toggle handleDrawerToggle to which will open the drawer */}
            <IconButton
              color="inherit"
              aria-label="open drawer"
              edge="start"
              onClick={handleDrawerToggle}
              sx={{ mr: 2, display: { sm: "none" } }}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h4" color="#4CA7DA" fontFamily="Shanti">
              RETYRN
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
              display: { xs: "block", sm: "none" },
              "& .MuiDrawer-paper": {
                boxSizing: "border-box",
                width: drawerWidth,
              },
            }}
          >
            {drawer}
          </Drawer>
          {/* When on Desktop view, the drawer is always shown. */}
          <Drawer
            variant="permanent"
            sx={{
              display: { xs: "none", sm: "block" },
              "& .MuiDrawer-paper": {
                boxSizing: "border-box",
                width: drawerWidth,
              },
            }}
            open
          >
            {drawer}
          </Drawer>
        </Box>

        {/* Main component to which displays whatever we want. */}
        <Toolbar></Toolbar>
      </Box>
    </ThemeProvider>
  );
}
