import {connect} from 'react-redux'

import './App.css';
import ScreenLayout from "./components/Layout";
import Routes from "./routes";

// Styles, Plugins and Fonts
import "./styles"

function App(props) {
  return (
    <div id="kt_body" className={`quick-panel-right demo-panel-right offcanvas-right header-fixed header-mobile-fixed subheader-enabled aside-enabled aside-fixed aside-minimize-hoverable ${!props.isOpened ? "aside-minimize" : ""}`}>
      <ScreenLayout>
          <Routes />
      </ScreenLayout>
    </div>
  );
}


const mapStateToProps = state => {
    return {
        isOpened: state.sidebar.isOpened
    }
}

export default connect(mapStateToProps, null)(App)
