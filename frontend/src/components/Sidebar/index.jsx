import React from 'react';
import { Link } from "react-router-dom";
import { MdViewList } from 'react-icons/md';
import { AiOutlineUserAdd, AiOutlineUsergroupAdd } from 'react-icons/ai';
import { GiMedallist } from 'react-icons/gi'


const Logo = props => {
    return (
        <a href="#" className="brand-logo">
            <img alt="Logo"
                 src="https://preview.keenthemes.com/keen/theme/demo1/dist/assets/media/logos/logo-1.svg"
                 className="h-30px"/>
        </a>
    )
}

const Toggle = props => {
    return (
        <button className="brand-toggle btn btn-sm px-0" id="kt_aside_toggle">
            <span className="svg-icon svg-icon svg-icon-xl">
                {/* --begin::Svg Icon | path:/keen/theme/demo1/dist/assets/media/svg/icons/Text/Toggle-Right.svg */}
                <svg xmlns="http://www.w3.org/2000/svg"
                     width="24px" height="24px" viewBox="0 0 24 24" version="1.1">
                    <g stroke="none" strokeWidth="1" fill="none" fillRule="evenodd">
                        <rect x="0" y="0" width="24" height="24"/>
                        <path fillRule="evenodd" clipRule="evenodd"
                              d="M22 11.5C22 12.3284 21.3284 13 20.5 13H3.5C2.6716 13 2 12.3284 2 11.5C2 10.6716 2.6716 10 3.5 10H20.5C21.3284 10 22 10.6716 22 11.5Z"
                              fill="black"/>
                        <path opacity="0.5" fillRule="evenodd" clipRule="evenodd"
                              d="M14.5 20C15.3284 20 16 19.3284 16 18.5C16 17.6716 15.3284 17 14.5 17H3.5C2.6716 17 2 17.6716 2 18.5C2 19.3284 2.6716 20 3.5 20H14.5ZM8.5 6C9.3284 6 10 5.32843 10 4.5C10 3.67157 9.3284 3 8.5 3H3.5C2.6716 3 2 3.67157 2 4.5C2 5.32843 2.6716 6 3.5 6H8.5Z"
                              fill="black"/>
                    </g>
                </svg>
                {/*    End Svg Icon*/}
            </span>
        </button>
    )
}

const Brand = props => {
    return (
        <div className="brand flex-column-auto" id="kt_brand">
            <Logo/>
            <Toggle/>
        </div>
    )
}


const Sidebar = props => {
    return (
        <div className="aside aside-left aside-fixed d-flex flex-column flex-row-auto " id="kt_aside">
            <Brand />
            {/*side links*/}
            <div className="text-center">
                <div className="pt-10 pb-5">
                    <AiOutlineUserAdd size={35} className="ico pr-3"/>
                    <Link className="text-col" to={"#"} >Add Member</Link> <br/>
                </div>
                <div className=" pb-5">
                    <MdViewList size={35} className="ico pr-3" />
                    <Link className="text-col" to={"#"} > List Member</Link><br/>
                </div>
                <div className="pb-5">
                    <AiOutlineUsergroupAdd size={35} className="ico pr-3"/>
                    <Link className="text-col" to={"#"}>Add Ministry</Link><br/>
                </div>
                <div className="">
                    <GiMedallist size={35} className="ico pr-3" />
                    <Link className="text-col" to={"#"}>List Ministry</Link>
                </div>
            </div>
        </div>
    )
}


export default Sidebar;