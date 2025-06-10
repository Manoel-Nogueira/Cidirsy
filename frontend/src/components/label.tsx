import type { ComponentProps, ReactNode } from "react"
import { twMerge } from "tailwind-merge"

interface LabelProps extends ComponentProps<"label"> {

    children: ReactNode,    

}

export function Label (props: LabelProps) {

    return (

        <label {...props} className={twMerge("pl-1", props.className)}>{props.children}</label>

    )

}