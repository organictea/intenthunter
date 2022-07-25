# coding=utf-8

from androguard.core.bytecodes.axml import AXMLPrinter
from zipfile import ZipFile


def extract_manifest(apk_file):
    with ZipFile(apk_file, "r") as zipObject:
        zipObject.extract(manifest_filename, working_dir)


def parse_manifest(manifest_file):
    with open(manifest_file, "rb") as fp:
        a = AXMLPrinter(fp.read())
    # Get the lxml.etree.Element from the AXMLPrinter:
    xml = a.get_xml_obj()
    # For example, get all uses-permission:
    # xml = a.get_xml()
    # print("List all activities")
    application = xml.findall("application")[0]
    activities = application.iter(tag="activity")
    receivers = application.iter(tag="receiver")
    services = application.iter(tag="service")
    exported_activities = []
    exported_receivers = []
    exported_services = []

    # for activity in activities:
    #     print(activity.attrib.get("{http://schemas.android.com/apk/res/android}name"))

    print("Exported activities")
    for activity in activities:
        if activity.attrib.get("{http://schemas.android.com/apk/res/android}exported") == "true" \
                or activity.attrib.get("exported") == "true" \
                or len(activity) != 0:
            if activity.attrib.get("{http://schemas.android.com/apk/res/android}name") is not None:
                exported_activities.append(activity.attrib.get("{http://schemas.android.com/apk/res/android}name"))
            elif activity.attrib.get("name") != "None":
                exported_activities.append(activity.attrib.get("name"))
            else:
                exported_activities.append("ComponentError")
    print(exported_activities)

    print("Exported receivers")
    for receiver in receivers:
        if receiver.attrib.get("{http://schemas.android.com/apk/res/android}exported") == "true" \
                or receiver.attrib.get("exported") == "true" \
                or len(receiver) != 0:
            if receiver.attrib.get("{http://schemas.android.com/apk/res/android}name") is not None:
                exported_receivers.append(receiver.attrib.get("{http://schemas.android.com/apk/res/android}name"))
            elif receiver.attrib.get("name") != "None":
                exported_receivers.append(receiver.attrib.get("name"))
            else:
                exported_receivers.append("ComponentError")
    print(exported_receivers)

    print("Exported services")
    for service in services:
        if service.attrib.get("{http://schemas.android.com/apk/res/android}exported") == "true" \
                or service.attrib.get("exported") == "true" \
                or len(service) != 0:
            if service.attrib.get("{http://schemas.android.com/apk/res/android}name") is not None:
                exported_services.append(service.attrib.get("{http://schemas.android.com/apk/res/android}name"))
            elif service.attrib.get("name") != "None":
                exported_services.append(service.attrib.get("name"))
            else:
                exported_services.append("ComponentError")
    print(exported_services)


if __name__ == '__main__':
    print('Intent Hunter')
    working_dir = "working_dir"
    manifest_filename = "AndroidManifest.xml"
    apk_filename = input("Enter the full path of the apk file: ")
    # apk_filename = "D:\\lab\\bugbounty\\mobile\\apps\\linkedin\\LinkedIn 4.1.707.apk"
    extract_manifest(apk_filename)
    manifest_relative_path = working_dir + "\\" + manifest_filename
    parse_manifest(manifest_relative_path)
