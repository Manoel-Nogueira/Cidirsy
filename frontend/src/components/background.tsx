import type { ComponentProps} from "react"
import { twMerge } from "tailwind-merge"
import BackgroundImage from "../assets/images/background2.jpg"

interface BackgroundProps extends ComponentProps<"image"> {


}

export function Background (props: BackgroundProps) {


    return (

        <img src={BackgroundImage} alt="background image" className={twMerge("h-full w-full absolute z-0 inset-0 bg-no-repeat bg-cover bg-center", props.className)}/>

    )

}