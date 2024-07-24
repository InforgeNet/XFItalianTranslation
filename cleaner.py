import xml.etree.ElementTree as ET

def remove_empty_phrases(xml_file):
	# Carica il file XML
	tree = ET.parse(xml_file)
	root = tree.getroot()

	# Trova tutti i genitori che hanno una tag <phrase> con addon_id="" e rimuove tali <phrase>
	phrases_to_remove = root.findall(".//phrase[@addon_id='']")
	for phrase in phrases_to_remove:
		for parent in root.iter():
			if phrase in list(parent):
				parent.remove(phrase)

	# Salva il file XML modificato
	tree.write(xml_file, encoding='utf-8', xml_declaration=True)

# Esempio di utilizzo
if __name__ == "__main__":
	xml_file = './language-italiano.xml'
	remove_empty_phrases(xml_file)