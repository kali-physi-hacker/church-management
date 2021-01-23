import React from 'react';


const Icon = props => {
    return (
        <span className={`${props.className} svg-icon ${props.active ? `svg-icon-${props.color}` : ""} svg-icon-${props.size} svg-icon-${props.color}`}>
            <svg xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" width="24px"
                 height={props.height} viewBox={props.viewBox} version="1.1">
                <g stroke={"none"} strokeWidth={"1"} fill={"none"}
                   fillRule={"evenodd"}>
                    {props.children}
                </g>
            </svg>
        </span>
    )
}


export default Icon;