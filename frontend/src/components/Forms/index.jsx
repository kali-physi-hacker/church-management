import React from 'react';


export const FormInput = props => {
    return (
        <>
            {props.label && <label className="col-xl-3 col-lg-3 col-form-label">{props.label}</label>}
            {
                props.containerClass ?
                    <div className={props.containerClass}>
                        <input
                            className={`form-control ${props.solid ? "form-control-solid" : ""} ${props.lg ? "form-control-lg" : ""} ${props.className}`}
                            type={props.type} value={props.value} placeholder={props.placeholder}/>
                        <span className="form-text text-muted">{props.infoText}</span>
                    </div> : <input
                        className={`form-control ${props.solid ? "form-control-solid" : ""} ${props.lg ? "form-control-lg" : ""} ${props.className}`}
                        type={props.type} value={props.value} placeholder={props.placeholder}/>
            }
        </>
    )
}


export const InputGroup = props => {
    return (
        <div className={`input-group ${props.solid ? "input-group-solid" : ""} ${props.lg ? "input-group-lg" : "" }`}>
            {props.children}
        </div>
    )
}

export const InputGroupPrepend = props => {
    return (
        <div
            className={`input-group-prepend ${props.solid ? "input-group-solid" : ""} ${props.lg ? "input-group-lg" : ""} ${props.className}`}>
            {props.text ?
                <span
                    className={`input-group-text ${props.groupTextClass}`}>
                {props.children}
            </span> :
                props.children
            }
        </div>
    )
}


export const FormGroup = props => {
    return (
        <div className="form-group row">
            {props.label && <label className="col-xl-3 col-lg-3 col-form-label">{props.label}</label>}
            {props.children}
        </div>
    )
}