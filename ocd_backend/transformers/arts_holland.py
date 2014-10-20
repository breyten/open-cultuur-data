from ocd_backend.transformers import BaseTransformer

class ArtsHollandTransformer(BaseTransformer):
    def transform_item(self, raw_item_content_type, raw_item, item):
        """Transforms a single item.

        The output of this method serves as input of a loader.

        :type raw_item_content_type: string
        :param raw_item_content_type: the content-type of the data
            retrieved from the source (e.g. ``application/json``)
        :type raw_item: string
        :param raw_item: the data in it's original format, as retrieved
            from the source (as a string)
        :type item: dict
        :param item: the deserialized item
        :returns: a tuple containing the new object id, the item sturctured
            for the combined index (as a dict) and the item item sturctured
            for the source specific index.
        """
    	transformed_item = {}

        config = {
    		"http://purl.org/artsholland/1.0/cidn": "id",
    		"http://purl.org/artsholland/1.0/genre": None,
    		"http://purl.org/artsholland/1.0/shortDescription": "introduction",
    		"http://purl.org/artsholland/1.0/languageNoProblem": None,
    		"http://purl.org/artsholland/1.0/productionType": None,
    		"http://purl.org/dc/terms/title": "title",
    		"http://purl.org/dc/terms/description": "description",
    		"http://purl.org/dc/terms/created": "created",
    		"http://purl.org/dc/terms/modified": "modified",
    		"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": None,
    		"http://www.w3.org/2002/07/owl#sameAs": None,
    	}
	       
    	for binding in item:
    		if not binding.get('hasValue'):
    			continue

    		value = binding.get('hasValue').get('value')
    		if not config[binding.get('property').get('value')]:
    			continue

    		if binding.get('hasValue').get('datatype')=='http://www.w3.org/2001/XMLSchema#dateTime':
    			import dateutil.parser
    			value = dateutil.parser.parse(value)
			
    		transformed_item[config[binding.get('property').get('value')]]=value

 
    	item = self.item_class(self.source_definition, raw_item_content_type,
                                   raw_item, transformed_item)

        self.add_resolveable_media_urls(item)

        return item.get_object_id(), item.get_combined_index_doc(), item.get_index_doc()


