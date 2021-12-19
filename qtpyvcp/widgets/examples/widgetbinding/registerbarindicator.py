# File: registerbarindicator.py
from bar_indicator import BarIndicatorBase

import QtDesigner


TOOLTIP = "A cool wiggly widget (Python)"
DOM_XML = """
<ui language='c++'>
    <widget class='BarIndicatorBase' name='BarIndicatorBase'>
        <property name='geometry'>
            <rect>
                <x>0</x>
                <y>0</y>
                <width>400</width>
                <height>200</height>
            </rect>
        </property>
        <property name='text'>
            <string>Hello, world</string>
        </property>
    </widget>
</ui>
"""

QPyDesignerCustomWidgetCollection.registerCustomWidget(BarIndicatorBase, module="bar_indicator",
                                                       tool_tip=TOOLTIP, xml=DOM_XML)