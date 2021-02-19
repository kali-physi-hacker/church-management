import React from 'react';


export const FormElement = props => {
    return (
        <>
            {props.label && <label className="col-xl-3 col-lg-3 col-form-label">{props.label}</label>}
            {
                props.containerClass ?
                    <div className={props.containerClass}>
                        {props.children}
                        <span
                            className={`form-text ${props.dangerInfo ? "text-danger" : "text-muted"}`}>{props.infoText}</span>
                    </div> : <>{props.children}</>
            }
        </>
    )
}

export const FormInput = props => {
    return (
        <FormElement {...props}>
            <input
                className={`form-control ${props.solid ? "form-control-solid" : ""} ${props.lg ? "form-control-lg" : ""} ${props.className}`}
                type={props.type} value={props.value} onChange={props.onChange} placeholder={props.placeholder}/>
        </FormElement>
    )
}

export const TextArea = props => {
    return (
        <FormElement {...props}>
            <textarea
                className={`form-control ${props.solid ? "form-control-solid" : ""} ${props.lg ? "form-control-lg" : ""} ${props.className}`}
                value={props.value} onChange={props.onChange}
                placeholder={props.placeholder} rows={props.rows} ></textarea>
        </FormElement>
    )
}


export const FormSelect = props => {
    return (
        <FormElement {...props}>
            <select onChange={props.onChange}
                    className={`form-control ${props.solid ? "form-control-solid" : ""} ${props.lg ? "form-control-lg" : ""} ${props.className}`}>
                <option>{props.title}</option>
                {
                    props.options.map((option, index) => (
                        <option key={index} value={option.value}>{option.label}</option>))
                }
            </select>
        </FormElement>
    )
}


export const InputGroup = props => {
    return (
        props.containerClass ? <div className={props.containerClass}>
            <div
                className={`input-group ${props.solid ? "input-group-solid" : ""} ${props.lg ? "input-group-lg" : ""}`}>
                {props.children}
            </div>
            <span className="form-text text-muted">{props.helpText}</span>
        </div> : <div
            className={`input-group ${props.solid ? "input-group-solid" : ""} ${props.lg ? "input-group-lg" : ""}`}>
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
            {/*<span*/}
            {/*    className="form-text text-muted">{props.helpText}</span>*/}
        </div>
    )
}