import Logo from "../assets/images/icon.png"
import { Label } from "../components/label"

export function Navbar () {

    return (

        <div className="h-24 w-full flex items-center justify-center bg-linear-to-t from-[#1A4D26] from-20% to-[#266F37]">
            
            <div className="flex items-center">

                <div>
                    <img src={Logo} alt="logo" className="h-[5.1rem] w-[5.1rem]"/>
                </div>

                <div>
                    <Label className="text-[#fbd916] text-[5rem] font-bahiana font-semibold text-shadow-lg uppercase">Cidirsy</Label>
                </div>

            </div>

        </div>

    )

}