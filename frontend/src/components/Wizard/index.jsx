import React from 'react';
import UserIcon from "../../Resources/Icons/User";
import ShieldProtectedIcon from "../../Resources/Icons/ShieldProtected";
import Thumbtack from "../../Resources/Icons/Thumbtack";
import LikeIcon from "../../Resources/Icons/Like";
import {FormGroup, FormInput, InputGroup, InputGroupPrepend} from "../Forms";
import ContactIcon from "../../Resources/Icons/Contact";


const WizardStep = props => {
    return (
        <div className="wizard-step" data-wizard-type="step" data-wizard-state={props.active ? 'current' : ''}>
            <div className="wizard-wrapper">
                <div className={"wizard-icon mr-4"}>
                    <props.icon size={"2x"} active={true}/>
                </div>
                <div className="wizard-label">
                    <div className="wizard-title">{props.title}</div>
                    <div className="wizard-desc">{props.description}</div>
                </div>
            </div>
        </div>
    )
}
const WizardNav = props => {
    return (
        <div className="wizard-nav">
            <div className="wizard-steps">
                <WizardStep active={true} icon={UserIcon} title={"Profile"}
                            description={"User's Personal Information"}/>
                <WizardStep icon={ShieldProtectedIcon} title={"Account"} description={"User's Account & Settings"}/>
                <WizardStep icon={Thumbtack} title={"Address"} description={"User's Shipping Address"}/>
                <WizardStep icon={LikeIcon} title={"Submission"} description={"Review and Submit"}/>
            </div>
        </div>
    )
}


const WizardForm = props => {
    return (
        <form className="form" id="kt_form">
            <div className="row justify-content-center">
                <div className="col-xl-9">
                    <div className="my-5 step" data-wizard-type="step-content" data-wizard-state="current">
                        <h5 className="text-dark font-weight-bold mb-10">User's Profile Details:</h5>
                        <div className="form-group row">
                            <label className="col-xl-3 col-lg-3 col-form-label text-left">Photo</label>
                            <div className="col-lg-9 col-xl-9">
                                <div className="image-input image-input-outline" id="kt_user_add_avatar">
                                    <div className="image-input-wrapper"
                                         style={{backgroundImage: "url(../../../../theme/demo1/dist/assets/media/users/150-1.jpg)"}}></div>
                                    <label
                                        className="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                                        data-action="change" data-toggle="tooltip" title=""
                                        data-original-title="Change avatar">
                                        <i className="fa fa-pen icon-sm text-muted"></i>
                                        <input type="file" name="profile_avatar" accept=".png, .jpg, .jpeg"/>
                                        <input type="hidden" name="profile_avatar_remove"/>
                                    </label>
                                    <span
                                        className="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                                        data-action="cancel" data-toggle="tooltip" title="Cancel avatar">
																							<i className="ki ki-bold-close icon-xs text-muted"></i>
																						</span>
                                </div>
                            </div>
                        </div>
                        <FormGroup>
                            <FormInput containerClass={"col-lg-9 col-xl-9"} solid lg type={"text"} label={"First Name"} placeholder={"First Name"}/>
                        </FormGroup>
                        <FormGroup>
                            <FormInput containerClass={"col-lg-9 col-xl-9"} solid lg type={"text"} label={"Last Name"} placeholder={"Last Name"}/>
                        </FormGroup>
                        <FormGroup>
                            <FormInput containerClass={"col-lg-9 col-xl-9"} solid lg type={"text"} label={"Company Name"} placeholder={"Company Name"} infoText={"If you want your invoices addressed to a company. Leave blank to use your full name."}/>
                        </FormGroup>


                        <FormGroup label={"Contact Phone"}>
                            <div className="col-lg-9 col-xl-9">
                                <InputGroup solid lg>
                                    <InputGroupPrepend text>
                                            <ContactIcon size={"2x"} color={"primary"} />
                                    </InputGroupPrepend>
                                    <FormInput solid lg type={"text"} placeholder={"Phone"} infoText={""}/>
                                </InputGroup>
                                <span
                                    className="form-text text-muted">Enter valid US phone number(e.g: 5678967456).</span>
                            </div>
                        </FormGroup>
                        <div className="form-group row">
                            <label className="col-xl-3 col-lg-3 col-form-label">Email Address</label>
                            <div className="col-lg-9 col-xl-9">
                                <div className="input-group input-group-solid input-group-lg">
                                    <div className="input-group-prepend">
																							<span
                                                                                                className="input-group-text">
																								<i className="la la-at"></i>
																							</span>
                                    </div>
                                    <input type="text" className="form-control form-control-solid form-control-lg"
                                           name="email" value="test@example.com"/>
                                </div>
                            </div>
                        </div>
                        <div className="form-group row">
                            <label className="col-xl-3 col-lg-3 col-form-label">Company Site</label>
                            <div className="col-lg-9 col-xl-9">
                                <div className="input-group input-group-solid input-group-lg">
                                    <input type="text" className="form-control form-control-solid form-control-lg"
                                           name="companywebsite" placeholder="Username" value="loop"/>
                                    <div className="input-group-append">
                                        <span className="input-group-text">.com</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    )
}


const WizardBody = props => {
    return (
        <div className={"card card-custom card-shadowless rounded-top-0"}>
            <div className={"card-body p-0"}>
                <div className="row justify-content-center py-8 px-8 py-lg-15 px-lg-10">
                    <div className="col-xl-12 col-xxl-10">
                        <WizardForm/>
                    </div>
                </div>
            </div>
        </div>
    )
}


const Wizard = props => {
    return (
        <div className="wizard wizard-4" id="kt_wizard" data-wizard-state="step-first" data-wizard-clickable="false">
            <WizardNav/>
            <WizardBody/>
        </div>
    )
}


export default Wizard;