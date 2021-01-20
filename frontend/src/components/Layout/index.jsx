import React from 'react';

// Custom Component Imports Here
import Sidebar from "../Sidebar";
import Header from "../Header";


const Content = props => {
    return (
        <div className="d-flex flex-column flex-row-fluid wrapper" id="kt_wrapper">
            <Header/>
            <div className="content d-flex flex-column flex-column-fluid" id="kt_content">
                {props.content}
            </div>
        </div>
    )
}


const AppRoot = props => {
    return (
        <div className="d-flex flex-column flex-root">
            <div className="d-flex flex-row flex-column-fluid page">
                <Sidebar/>
            </div>
            {props.children}
        </div>
    )
}


const PageLayout = props => {
    return (
        <AppRoot>
            <Content content={props.children} />
        </AppRoot>
    )
}


export default PageLayout