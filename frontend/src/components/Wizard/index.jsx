import React, {useState, useEffect, useContext, useReducer} from 'react';
import axios from "axios";
import {useHistory} from 'react-router-dom';

import {FormElement, FormGroup, FormInput, FormSelect, InputGroup, InputGroupPrepend} from "../Forms";
import UserIcon from "../../Resources/Icons/User";
import ShieldProtectedIcon from "../../Resources/Icons/ShieldProtected";
import UserGroupIcon from "../../Resources/Icons/UserGroup";
import ContactIcon from "../../Resources/Icons/Contact";
import MailIcon from "../../Resources/Icons/Mail";
import ArrowLeftIcon from "../../Resources/Icons/ArrowLeft";
import CheckIcon from "../../Resources/Icons/Check";
import ArrowRightIcon from "../../Resources/Icons/ArrowRight";


const initialState = {
    // User (Church Member) fields
    first_name: null,
    middle_name: null,
    last_name: null,
    email: null,
    age: null,
    date_of_birth: null,
    is_student: false,
    ministry: null,
    contact_1: null,
    contact_2: null,
    mothers_contact: null,
    fathers_contact: null,
    location: null,
    occupation: null,
    marital_status: "SINGLE",

    // Other fields here
    // fieldRequiredErrorMsg: "This field is required"

}

const reducer = (state = initialState, action) => {
    switch (action.type) {
        case "ADD_FIELD":
            return {
                ...state, ...action
            }
        default:
            return state
    }
}


const AddUserContext = React.createContext()


const WizardStep = props => {
    return (
        <div className="wizard-step" data-wizard-type="step" data-wizard-state={props.current}>
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
    const steps = [
        (props) => {
            return <WizardStep {...props} icon={UserIcon} title={"Bio"}
                               description={"User's Personal Bio Information"}/>
        },
        (props) => {
            return <WizardStep {...props} icon={ShieldProtectedIcon} title={"Contact"}
                               description={"User's contact information"}/>
        },
        (props) => {
            return <WizardStep {...props} icon={UserGroupIcon} title={"Family"} description={"User's family details"}/>
        }
    ]
    return (
        <div className="wizard-nav">
            <div className="wizard-steps">
                {
                    steps.map((Step, index) => (
                        <Step {...props} current={index === props.currentIndex ? "current" : ""} key={index}/>)
                    )
                }
            </div>
        </div>
    )
}

const WizardActions = props => {
    return (
        <div className="d-flex justify-content-between border-top pt-10 mt-15">
            <div className="mr-2">
                <button onClick={props.previous} style={{display: props.currentIndex > 0 ? "inline-block" : "none"}}
                        type="button" id="prev-step"
                        className="btn btn-light-primary font-weight-bolder px-10 py-3"
                        data-wizard-type="action-prev">
                    <ArrowLeftIcon/> Previous
                </button>
            </div>
            <div>
                <button onClick={props.submit} style={{display: props.currentIndex == 2 ? "inline-block" : "none"}}
                        onClick={props.submit}
                        type="button" className="btn btn-success font-weight-bolder px-10 py-3"
                        data-wizard-type="action-submit">Submit
                    <CheckIcon/>
                </button>
                <button style={{display: props.currentIndex < 2 ? "inline-block" : "none"}} onClick={props.next}
                        type="button" id="next-step"
                        className="btn btn-primary font-weight-bolder px-10 py-3"
                        data-wizard-type="action-next">Next
                    <ArrowRightIcon/>
                </button>
            </div>
        </div>
    )
}


const WizardStepContent = props => {
    return (
        <div className="my-5 step" data-wizard-type="step-content" data-wizard-state={props.current}>
            <h5 className="text-dark font-weight-bold mb-10">{props.title}</h5>
            {props.children}
        </div>
    )
}


const MinistryInput = () => {
    const [ministries, setMinistries] = useState([])

    const fieldsContext = useContext(AddUserContext)
    const dispatch = fieldsContext.dispatchFields;

    const {
        ministry
    } = fieldsContext.fields

    useEffect(() => {
        axios.get("/ministry/")
            .then(response => {
                const ministryOptions = []
                response.data.ministries.map(ministry => {
                    delete Object.assign(ministry, {["value"]: ministry["id"]})["id"];
                    delete Object.assign(ministry, {["label"]: ministry["name"]})["name"];
                    ministryOptions.push(ministry)
                })
                setMinistries(ministryOptions)
            })
            .catch(error => {
                console.log(error.response)
            })
    }, [])

    return (
        <FormGroup>
            <FormSelect value={ministry} onChange={e=> dispatch({type: "ADD_FIELD", ministry: parseInt(e.target.value)})} title={"Select Ministry"} options={ministries} containerClass={"col-lg-9 col-xl-9"} solid lg
                        label={"Ministry"}/>
        </FormGroup>
    )
}

const WizardStepContent1 = props => {

    const fieldsContext = useContext(AddUserContext)

    const dispatch = fieldsContext.dispatchFields;

    const {
        first_name,
        middle_name,
        last_name,
        email,
        age,
        date_of_birth,
        is_student,
        fieldRequiredErrorMsg
    } = fieldsContext.fields

    return (
        <WizardStepContent title={"User's Profile Details:"} current={props.current}>
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
                <FormInput value={first_name} onChange={e => dispatch({type: "ADD_FIELD", first_name: e.target.value})}
                           containerClass={"col-lg-9 col-xl-9"} solid lg type={"text"}
                           label={"First Name"} placeholder={"First Name"}
                           infoText={"Something"}
                />
            </FormGroup>
            <FormGroup>
                <FormInput value={middle_name}
                           onChange={e => dispatch({type: "ADD_FIELD", middle_name: e.target.value})}
                           containerClass={"col-lg-9 col-xl-9"} solid lg type={"text"}
                           label={"Middle Name"} placeholder={"Middle Name"}
                           infoText={"Empty values are accepted"}/>
            </FormGroup>
            <FormGroup>
                <FormInput value={last_name} onChange={e => dispatch({type: "ADD_FIELD", last_name: e.target.value})}
                           containerClass={"col-lg-9 col-xl-9"} solid lg type={"text"}
                           label={"Last Name"} placeholder={"Last Name"}/>
            </FormGroup>
            <FormGroup label={"Email Address"}>
                <div className="col-lg-9 col-xl-9">
                    <InputGroup solid lg>
                        <InputGroupPrepend text>
                            <MailIcon size={"2x"} color={"secondary"}/>
                        </InputGroupPrepend>
                        <FormInput value={email} onChange={e => dispatch({type: "ADD_FIELD", email: e.target.value})}
                                   solid lg type={"text"} placeholder={"someone@email.com"} infoText={""}/>
                    </InputGroup>
                </div>
            </FormGroup>
            <FormGroup>
                <FormInput value={age} onChange={e => dispatch({type: "ADD_FIELD", age: e.target.value})}
                           containerClass={"col-lg-2 col-xl-2"} solid lg type={"text"} label={"Age"}
                           placeholder={"E.g 21"}/>
            </FormGroup>
            <FormGroup>
                <FormInput value={date_of_birth}
                           onChange={e => dispatch({type: "ADD_FIELD", date_of_birth: e.target.value})}
                           containerClass={"col-lg-9 col-xl-9"} solid lg type={"date"}
                           label={"Date of birth"} placeholder={""}/>
            </FormGroup>
            <FormGroup>
                <FormElement containerClass={"col-lg-9 col-xl-9"} solid lg label={"Student"}>
                    <div className="radio-inline">
                        <label className="radio radio-rounded">
                            <input checked={is_student} onChange={e => dispatch({type: "ADD_FIELD", is_student: true})}
                                   type="radio" name="is_student"/>
                            <span></span>Yes</label>
                        <label className="radio radio-rounded">
                            <input checked={!is_student}
                                   onChange={e => dispatch({type: "ADD_FIELD", is_student: false})}
                                   type="radio" name="is_student"/>
                            <span></span>No</label>
                    </div>
                </FormElement>
            </FormGroup>
            <MinistryInput/>

        </WizardStepContent>
    )
}


const WizardStepContent2 = props => {
    const fieldsContext = useContext(AddUserContext)

    const dispatch = fieldsContext.dispatchFields;

    const {
        contact_1,
        contact_2,
        mothers_contact,
        fathers_contact,
        location
    } = fieldsContext.fields
    return (
        <WizardStepContent title={"User's contact details"} current={props.current}>
            <FormGroup label={"Contact Phone 1"}>
                <InputGroup helpText={"Enter valid US phone number(e.g: 5678967456)."}
                            containerClass={"col-lg-5 col-xl-5"} solid lg>
                    <InputGroupPrepend text>
                        <ContactIcon size={"2x"} color={"secondary"}/>
                    </InputGroupPrepend>
                    <FormInput value={contact_1}
                               onChange={e => dispatch({type: "ADD_FIELD", contact_1: e.target.value})}
                               solid lg type={"tel"}
                               placeholder={"+233123456789"} infoText={""}/>
                </InputGroup>
            </FormGroup>
            <FormGroup label={"Contact Phone 2"}>
                <InputGroup helpText={"Enter valid US phone number(e.g: 5678967456)."}
                            containerClass={"col-lg-5 col-xl-5"} solid lg>
                    <InputGroupPrepend text>
                        <ContactIcon size={"2x"} color={"secondary"}/>
                    </InputGroupPrepend>
                    <FormInput value={contact_2}
                               onChange={e => dispatch({type: "ADD_FIELD", contact_2: e.target.value})}
                               solid lg type={"tel"}
                               placeholder={"+233123456789"} infoText={""}/>
                </InputGroup>
            </FormGroup>
            <FormGroup label={"Mother's Contact"}>
                <InputGroup helpText={"Enter valid US phone number(e.g: 5678967456)."}
                            containerClass={"col-lg-5 col-xl-5"} solid lg>
                    <InputGroupPrepend text>
                        <ContactIcon size={"2x"} color={"secondary"}/>
                    </InputGroupPrepend>
                    <FormInput value={mothers_contact}
                               onChange={e => dispatch({type: "ADD_FIELD", mothers_contact: e.target.value})}
                               solid lg type={"tel"}
                               placeholder={"+233123456789"} infoText={""}/>
                </InputGroup>
            </FormGroup>
            <FormGroup label={"Father's Contact"}>
                <InputGroup helpText={"Enter valid US phone number(e.g: 5678967456)."}
                            containerClass={"col-lg-5 col-xl-5"} solid lg>
                    <InputGroupPrepend text>
                        <ContactIcon size={"2x"} color={"secondary"}/>
                    </InputGroupPrepend>
                    <FormInput value={fathers_contact}
                               onChange={e => dispatch({type: "ADD_FIELD", fathers_contact: e.target.value})}
                               solid lg type={"tel"}
                               placeholder={"+233123456789"} infoText={""}/>
                </InputGroup>
            </FormGroup>
            <FormGroup>
                <FormInput value={location} onChange={e => dispatch({type: "ADD_FIELD", location: e.target.value})}
                           containerClass={"col-lg-9 col-xl-9"} solid lg
                           type={"text"}
                           label={"Residential Location"} placeholder={"E.g Abeka"}/>
            </FormGroup>
        </WizardStepContent>
    )
}


const WizardStepContent3 = props => {
    const [isMarried ,setIsMarried] = useState(false);
    const fieldsContext = useContext(AddUserContext)

    const dispatch = fieldsContext.dispatchFields;

    const {
        occupation,
        marital_status
    } = fieldsContext.fields

    return (
        <WizardStepContent title={"User's family details"} current={props.current}>
            <FormGroup>
                <FormInput value={occupation} onChange={e => dispatch({type: "ADD_FIELD", occupation: e.target.value})}
                           containerClass={"col-lg-9 col-xl-9"} solid lg type={"text"}
                           label={"Occupation"} placeholder={"E.g Teacher"}/>
            </FormGroup>
            <FormGroup>
                <FormElement containerClass={"col-lg-9 col-xl-9"} solid lg type={"date"} label={"Marital Status"}>
                    <div className="radio-inline">
                        <label className="radio radio-rounded">
                            <input value={"SINGLE"} type="radio" checked={!isMarried}
                                   onChange={e => {dispatch({type: "ADD_FIELD", marital_status: e.target.value}); setIsMarried(false)}}
                                   name="married"/>
                            <span></span>Single</label>
                        <label className="radio radio-rounded">
                            <input value={"MARRIED"} type="radio" checked={isMarried}
                                   onChange={e => {dispatch({type: "ADD_FIELD", marital_status: e.target.value}); setIsMarried(true)}}
                                   name="married"/>
                            <span></span>Married</label>
                    </div>

                </FormElement>
            </FormGroup>
            <FormGroup>
                <FormInput containerClass={"col-lg-2 col-xl-2"} solid lg type={"text"}
                           label={"No of Children"} placeholder={"E.g 5"}/>
            </FormGroup>

        </WizardStepContent>
    )
}

const StepContentContainer = props => {
    return (
        <div className="row justify-content-center">
            <div className="col-xl-9">
                {
                    props.steps.map((Child, index) => (
                        <Child current={index === props.current ? "current" : ""} key={index}/>))
                }
            </div>
        </div>
    )
}
const WizardForm = props => {
    return (
        <form className="form" id="kt_form">
            <StepContentContainer current={props.currentIndex} steps={props.steps}>
            </StepContentContainer>
            <WizardActions submit={props.addUser} currentIndex={props.currentIndex} next={props.nextStep}
                           previous={props.prevStep}/>
        </form>
    )
}


const WizardBody = props => {
    return (
        <div className={"card card-custom card-shadowless rounded-top-0"}>
            <div className={"card-body p-0"}>
                <div className="row justify-content-center py-8 px-8 py-lg-15 px-lg-10">
                    <div className="col-xl-12 col-xxl-10">
                        <WizardForm {...props} />
                    </div>
                </div>
            </div>
        </div>
    )
}


const Wizard = props => {

    const history = useHistory()

    const [fields, dispatchFields] = useReducer(reducer, initialState)

    const [currentIndex, setCurrentIndex] = useState(0);

    const steps = [WizardStepContent1, WizardStepContent2, WizardStepContent3]

    const nextStep = e => {
        if (currentIndex < steps.length) {
            setCurrentIndex(currentIndex + 1)
        }
    }

    const prevStep = e => {
        if (currentIndex > 0) {
            setCurrentIndex(currentIndex - 1)
        }
    }

    const addUser = () => {
        delete fields.type
        console.log(fields)
        axios.post("/member/", fields)
            .then(response => {
                history.push("/member/list/")
            })
            .catch(error => {
                console.log(error.response)
            })
    }

    const propValues = {steps, currentIndex, nextStep, prevStep, addUser}

    return (
        <div className="wizard wizard-4" id="kt_wizard" data-wizard-state="step-first"
             data-wizard-clickable="false">
            <AddUserContext.Provider value={{fields: fields, dispatchFields: dispatchFields}}>
                <WizardNav {...propValues} />
                <WizardBody {...propValues} />
            </AddUserContext.Provider>
        </div>
    )
}


export default Wizard;