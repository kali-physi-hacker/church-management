import React, {useReducer} from "react";
import Wizard from "../../../components/Wizard";
import SubHeader from "../../../components/Subheader";


const CompleteDialog = () => {
    return (
        <div className="swal2-container swal2-center swal2-backdrop-show" style={{overflowY: "auto"}}>
            <div aria-labelledby="swal2-title" aria-describedby="swal2-content"
                 className="swal2-popup swal2-modal swal2-icon-success swal2-show" tabIndex="-1" role="dialog"
                 aria-live="assertive" aria-modal="true" style={{display: "flex"}}>
                <div className="swal2-header">
                    <div className="swal2-icon swal2-success swal2-icon-show" style={{display: "flex"}}>
                        <div className="swal2-success-circular-line-left"
                             style={{backgroundColor: "rgb(255, 255, 255)"}}></div>
                        <span className="swal2-success-line-tip"></span> <span
                        className="swal2-success-line-long"></span>
                        <div className="swal2-success-ring"></div>
                        <div className="swal2-success-fix" style={{backgroundColor: "rgb(255, 255, 255)"}}></div>
                        <div className="swal2-success-circular-line-right"
                             style={{backgroundColor: "rgb(255, 255, 255)"}}></div>
                    </div>
                </div>
                <div className="swal2-content">
                    <div id="swal2-content" className="swal2-html-container" style={{display: "block"}}>All is good!
                        Please
                        confirm the form submission.
                    </div>
                    <div className="swal2-validation-message" id="swal2-validation-message"></div>
                </div>
                <div className="swal2-actions">
                    <div className="swal2-loader"></div>
                    <button type="button" className="swal2-confirm btn font-weight-bold btn-primary"
                            style={{display: "inline-block"}} aria-label="">Yes, submit!
                    </button>
                    <button type="button" className="swal2-cancel btn font-weight-bold btn-default"
                            style={{display: "inline-block"}} aria-label="">No, cancel
                    </button>
                </div>
            </div>
        </div>
    )
}


const AddPage = () => {
    return (
        <>
            <SubHeader title={"Add User"} description={"Enter User's Information"}/>
            <div className={"d-flex flex-column-fluid"}>
                <div className={"container"}>
                    <div className={"card card-custom card-transparent"}>
                        <div className={"card-body p-0"}>
                            <Wizard/>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}


export default AddPage;